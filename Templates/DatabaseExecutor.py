# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from concurrent.futures import ThreadPoolExecutor

import cx_Oracle
from kivy.app import App
from Templates.ErrorHandlers import *
from Backgrounds import DatabaseTask


def execute_in_background(function):
    def wrapped(*args, **kwargs):
        DatabaseTask(function, *args, **kwargs).start()

    return wrapped


class DatabaseConnection(object):
    def __init__(self, url='teter/fx0507@127.10.0.1/Grafiki'):
        super(DatabaseConnection, self).__init__()
        self.url = url
        self.connection = None
        self.database_cursor = None
        self.connection_error_popup = ConnectionErrorPopup("Error occured while connecting to database.\n"
                                                           "Please, check your internet connection.")
        self.connect_to_database()

    @handle_connection_errors
    def connect_to_database(self):
        self.connection = cx_Oracle.connect(self.url)
        self.database_cursor = self.connection.cursor()

    @handle_connection_errors
    def fetch_query(self, sql_command):
        return self.database_cursor.execute(sql_command)

    @handle_connection_errors
    def execute_command(self, sql_command):
        self.database_cursor.execute(sql_command)
        self.connection.commit()

    def connection_error(self, interrupted_func):
        self.connection_error_popup.open()
        self.connect_to_database()
        interrupted_func()


class SqlCommandsExecutor(object):
    def __init__(self, bag):
        super(SqlCommandsExecutor, self).__init__()
        self.bag = bag

    @execute_in_background
    def fetch_logins(self):
        users_logins = {}
        query = DatabaseConnection().fetch_query("select login, password from Instruktorzy")
        if query:
            for result in query:
                users_logins[result[0]] = result[1]
                print result
            return {'users_logins': users_logins}
