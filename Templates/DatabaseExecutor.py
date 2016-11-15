# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

import cx_Oracle
from kivy.app import App
from Templates.ErrorHandlers import *


class DatabaseConnection(object):
    def __init__(self, url='teter/fx0507@127.0.0.1/Grafiki'):
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

    def connection_error(self):
        self.connection_error_popup.open()


class SqlCommandsExecutor(object):
    def __init__(self):
        super(SqlCommandsExecutor, self).__init__()
        self.database = DatabaseConnection()

    def fetch_logins(self):
        users_logins = {}
        query = self.database.fetch_query("select login, password from Instruktorzy")
        if query:
            for result in query:
                users_logins[result[0]] = result[1]
                print query
            return {'users_logins': users_logins}
