# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from adventureskiing.Config.config import privileges
from adventureskiing.Database.MySQL.SqlCmdChoosers import EarningsCmdChooser
from adventureskiing.Utils.Users import User
from adventureskiing.Utils.cennik import cennik
from common_database.MySqlConnection import DatabaseConnection, sys


# TODO refactoring kwargs to params!!!!
from common_utilities.Utilities import ignored


class SqlCommands(object):
    """Class storing Database commands as static methods. """

    @staticmethod
    def fetch_logins(username, password, *args, **kwargs):
        """ Template method to execute sql commands,
            methods needs to get *args, **kwargs """
        try:
            query = DatabaseConnection().fetch_query(
                "select imie, nazwisko, id, uprawnienia "
                "from instruktorzy "
                "where login = '{}' and password = '{}'".format(username, password))
            return query[0]
        except:
            return None

    @staticmethod
    def get_daily_graph(day, user, *args, **kwargs):
        try:
            query = DatabaseConnection().fetch_query("select godzina, imie, wiek, ilosc_osob, id "
                                                     "from lekcja "
                                                     "where id_instruktora = {} "
                                                     "and data = STR_TO_DATE('{}', '%Y/%m/%d')".format(user.id, day))
            return {result[0]: ("{}.00 | {}, {}lat. #{}os.".format(*result[:-1]), result[-1]) for result in query}
        except:
            print "Couldnt read daily graph {}".format(sys.exc_info()[0])

    @staticmethod
    def get_all_users(*args, **kwargs):
        try:
            query = DatabaseConnection().fetch_query("select imie, nazwisko, id, uprawnienia from instruktorzy")
            return {name: User(user_id=user_id, permission=privileges, name=name, lastname=lastname)
                    for name, lastname, user_id, privileges in query}
        except:
            print 'Couldnt get all users'

    @staticmethod
    def insert_new_lesson(number_of_people, *args, **kwargs): # TODO bezsensu, refactoring !!
        try:
            cmd = "Select id from lekcja where id_instruktora = {instructor} and " \
                  "godzina = {godzina} and " \
                  "data = STR_TO_DATE('{data}', '%Y/%m/%d')".format(instructor=kwargs['user'].id,
                                                                    godzina=kwargs['hour'], data=kwargs['date'])
            query = DatabaseConnection().fetch_query(cmd)
            if len(query) != 0: return False
            if kwargs.get('name').isalpha() and kwargs.get('age').isdigit():
                if not kwargs['lesson_id'] == "0":
                    DatabaseConnection().execute_command("delete from lekcja where id = {}".format(kwargs['lesson_id']))

                DatabaseConnection().execute_command("insert into lekcja "
                                                     "(imie, godzina, data, ilosc_osob, koszt, id_instruktora, wiek) "
                                                     "values ('{imie}', {godzina}, STR_TO_DATE('{data}', '%Y/%m/%d'), "
                                                     "{ilosc_osob}, {koszt}, {id_instruktora}, {wiek})"
                                                     .format(imie=kwargs['name'], godzina=kwargs['hour'],
                                                             data=kwargs['date'], ilosc_osob=number_of_people,
                                                             koszt=cennik.get(int(number_of_people), 0),
                                                             id_instruktora=kwargs['user'].id, wiek=kwargs['age']))
                return True
        except:
            print "Couldnt add lesson {}".format(sys.exc_info()[0])

    @staticmethod
    def remove_lesson(*args, **kwargs):
        try:
            if kwargs['lesson_id'] != "0":
                DatabaseConnection().execute_command("delete from lekcja where id = {}".format(kwargs['lesson_id']))
        except:
            print "Couldnt remove lesson from Database {}".format(sys.exc_info()[0])

    @staticmethod
    def get_unoccupied(date, hour, *args, **kwargs):
        try:
            query = DatabaseConnection().fetch_query("select imie, nazwisko, id from instruktorzy")
            all_instructors = set(query)
            query = DatabaseConnection().fetch_query("select instruktorzy.imie, instruktorzy.nazwisko, "
                                                     "instruktorzy.id from instruktorzy join "
                                                     "lekcja on instruktorzy.id = lekcja.id_instruktora where data = "
                                                     "STR_TO_DATE('{}', '%Y/%m/%d') and godzina = {}".format(date, hour))
            busy_instructors = set(query)
            return [User(name=imie, lastname=nazwisko, user_id=id, permission='User')
                    for imie, nazwisko, id in list(all_instructors - busy_instructors)]
        except:
            print "Error loading unoccupied instructors {}".format(sys.exc_info()[0])

    @staticmethod
    def get_earnings(period, user, *args, **kwargs):
        with ignored(Exception):
            cmd = EarningsCmdChooser().get_earnings_cmd_from[period[0]](period, user)
            query = DatabaseConnection().fetch_query(cmd)
            return query[0][0]

    @staticmethod
    def password_update(old_pw, new_pw, user, *args, **kwargs):
        cmd = "Update instruktorzy set password = '{}' where id = {} and password = '{}'".format(new_pw,
                                                                                                 user.id,
                                                                                                 old_pw)
        DatabaseConnection().execute_command(cmd)
        query = DatabaseConnection().fetch_query("Select password from instruktorzy where id = '{}'".format(user.id))
        return True if query[0][0] == str(new_pw) else False

    @staticmethod
    def create_user(firstname, lastname, login, *args, **kwargs):
        try:
            if firstname.isalpha() and login.isalnum():
                query = DatabaseConnection().fetch_query(
                    "Select login from instruktorzy where login='{}'".format(login))
                with ignored(IndexError):
                    if query[0][0] == login: return False
                cmd = "Insert into instruktorzy (login, password, imie, nazwisko, uprawnienia) values " \
                      "('{login}', '{password}', '{firstname}', '{lastname}', 'User')".format(firstname=firstname,
                                                                                              lastname=lastname,
                                                                                              login=login,
                                                                                              password=hash(login))
                DatabaseConnection().execute_command(cmd)
                query = DatabaseConnection().fetch_query(
                    "Select login from instruktorzy where login='{}'".format(login))
                if query[0][0] == login: return True
        except:
            return None

    @staticmethod
    def remove_user(user, *args, **kwargs):
        with ignored(Exception):
            DatabaseConnection().execute_command('Delete from instruktorzy where id={}'.format(user.id))
            query = DatabaseConnection().fetch_query('Select id from instruktorzy where id={}'.format(user.id))
            if len(query) > 0: return False
            return True

    @staticmethod
    def change_permissions(*args, **kwargs):
        with ignored(Exception):
            user_button, permission_button = args
            if permission_button in privileges:
                DatabaseConnection().execute_command(
                    "Update instruktorzy set uprawnienia = '{}' where id = {}".format(permission_button,
                                                                                      user_button.id))
                query = DatabaseConnection().fetch_query(
                    'Select uprawnienia from instruktorzy where id = {}'.format(user_button.id))
                return True if query[0][0] == permission_button else False
