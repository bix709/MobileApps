# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from common_database.DatabaseConnection import DatabaseConnection
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
            query = DatabaseConnection().fetch_query("select godzina, imie, wiek, ilosc_osob "
                                                     "from lekcja "
                                                     "where id_instruktora = {} "
                                                     "and data = TO_DATE('{}', 'yyyy/mm/dd')".format(user.id, day))
            if query:
                for result in query:
                    busy_hours[result[0]] = "{}.00 | {}, {}lat. #{}os.".format(*result)
                    print busy_hours[result[0]]
        finally:
            return busy_hours
