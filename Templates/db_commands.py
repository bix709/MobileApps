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
    def fetch_logins(*args, **kwargs):
        """ Template method to execute sql commands,
            methods needs to get *args, **kwargs, and
            to be decorated with @update_bag_with_result """
        users_logins = {}
        query = DatabaseConnection().fetch_query("select login, password from Instruktorzy")
        if query:
            for result in query:
                users_logins[result[0]] = result[1]
            return users_logins
