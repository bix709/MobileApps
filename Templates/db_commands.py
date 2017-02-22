# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from Templates.SqlCmdChoosers import EarningsCmdChooser
from Templates.cennik import cennik
from Templates.Users import User
from common_database.DatabaseConnection import DatabaseConnection, sys
from common_tools.ThreadSynchronization import mark_task_as_done


class SqlCommands(object):
    """Class storing database commands as static methods. """

    @staticmethod
    @mark_task_as_done
    def fetch_logins(username, password, *args, **kwargs):
        """ Template method to execute sql commands,
            methods needs to get *args, **kwargs, and
            to be decorated with @update_bag_with_result """
        try:
            query = DatabaseConnection().fetch_query(
                "select imie, id, uprawnienia "
                "from Instruktorzy "
                "where login = '{}' and password = '{}'".format(username, password))
            if query:
                return [result for result in query][0]
        except:
            return None

    @staticmethod
    @mark_task_as_done
    def get_daily_graph(day, user, *args, **kwargs):
        busy_hours = {}
        try:
            query = DatabaseConnection().fetch_query("select godzina, imie, wiek, ilosc_osob, id "
                                                     "from lekcja "
                                                     "where id_instruktora = {} "
                                                     "and data = TO_DATE('{}', 'yyyy/mm/dd')".format(user.id, day))
            if query:
                for result in query:
                    busy_hours[result[0]] = ("{}.00 | {}, {}lat. #{}os.".format(*result[:-1]), result[-1])
        except:
            print "Couldnt read daily graph {}".format(sys.exc_info()[0])
        finally:
            return busy_hours

    @staticmethod
    @mark_task_as_done
    def get_all_users(*args, **kwargs):
        users = {}
        try:
            query = DatabaseConnection().fetch_query("select imie, id, uprawnienia from instruktorzy")
            if query:
                for output in query:
                    name, user_id, privileges = output
                    users[name] = User(user_id=user_id, permission=privileges, name=name)
        finally:
            return users

    @staticmethod
    @mark_task_as_done
    def insert_new_lesson(*args, **kwargs):
        try:
            if kwargs['lesson_id'] == "0":
                query = DatabaseConnection().fetch_query("select lesson_id_seq.nextval from dual")
                if query:
                    kwargs['lesson_id'] = [result for result in query][0][0]
            else:
                DatabaseConnection().execute_command("delete from lekcja where id = {}".format(kwargs['lesson_id']))

            ilosc_osob = kwargs['number_of_people']
            DatabaseConnection().execute_command("insert into lekcja "
                                                 "(imie, godzina, data, ilosc_osob, koszt, id, id_instruktora, wiek) "
                                                 "values ('{imie}', {godzina}, TO_DATE('{data}', 'yyyy/mm/dd'), "
                                                 "{ilosc_osob}, {koszt}, {lesson_id}, {id_instruktora}, {wiek})"
                                                 .format(imie=kwargs['name'], godzina=kwargs['hour'],
                                                         data=kwargs['date'], ilosc_osob=ilosc_osob,
                                                         koszt=cennik[int(ilosc_osob)], lesson_id=kwargs['lesson_id'],
                                                         id_instruktora=kwargs['user'].id, wiek=kwargs['age']))
        except:
            print "Couldnt add lesson {}".format(sys.exc_info()[0])

    @staticmethod
    @mark_task_as_done
    def remove_lesson(*args, **kwargs):
        try:
            if kwargs['lesson_id'] != "0":
                DatabaseConnection().execute_command("delete from lekcja where id = {}".format(kwargs['lesson_id']))
        except:
            print "Couldnt remove lesson from database {}".format(sys.exc_info()[0])

    @staticmethod
    @mark_task_as_done
    def get_unoccupied(date, hour, *args, **kwargs):
        unoccupied_instructors = []
        try:
            all_instructors = busy_instructors = {}
            query = DatabaseConnection().fetch_query("select imie, id from instruktorzy")

            if query:
                all_instructors = set([result for result in query])
            query = DatabaseConnection().fetch_query("select instruktorzy.imie, instruktorzy.id from instruktorzy join "
                                                     "lekcja on instruktorzy.id = lekcja.id_instruktora where data = "
                                                     "TO_DATE('{}', 'yyyy/mm/dd') and godzina = {}".format(date, hour))
            if query:
                busy_instructors = set([result for result in query])
            for instructor in list(all_instructors - busy_instructors):
                unoccupied_instructors.append(User(name=instructor[0], user_id=instructor[1], permission="User"))
            return unoccupied_instructors
        except:
            print "Error loading unoccupied instructors {}".format(sys.exc_info()[0])

    @staticmethod
    @mark_task_as_done
    def get_earnings(period, user, *args, **kwargs):
        try:
            cmd = EarningsCmdChooser().get_earnings_cmd_from[period[0]](period, user)
            query = DatabaseConnection().fetch_query(cmd)
            if query:
                return [result for result in query][0][0]
        except:
            print "Couldnt get earnings from date. {}".format(sys.exc_info()[0])
            return None

    @staticmethod
    @mark_task_as_done
    def password_update(old_pw, new_pw, user, *args, **kwargs):
        cmd = "Update instruktorzy set password = '{}' where id = {} and password = '{}'".format(new_pw,
                                                                                                 user.id,
                                                                                                 old_pw)
        DatabaseConnection().execute_command(cmd)
        query = DatabaseConnection().fetch_query("Select password from instruktorzy where id = '{}'".format(user.id))
        if query:
            return True if [result for result in query][0][0] == str(new_pw) else False
