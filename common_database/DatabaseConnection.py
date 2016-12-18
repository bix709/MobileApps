# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from time import sleep

import cx_Oracle

from common_database.ErrorHandlers import *


class DatabaseConnection(object):
    def __init__(self, url='teter/fx0507@127.0.0.1/Grafiki'):
        super(DatabaseConnection, self).__init__()
        self.url = url
        self.connection = None
        self.database_cursor = None
        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.connection = cx_Oracle.connect(self.url)
            self.database_cursor = self.connection.cursor()
        except:
            self.connection_error()

    def fetch_query(self, sql_command):
        return self.database_cursor.execute(sql_command)

    def execute_command(self, sql_command):
        self.database_cursor.execute(sql_command)
        self.connection.commit()

    def connection_error(self):
        issue = ConnectionError()
        issue.display_connection_error_label()
        while not self.connected():
            sleep(1)
        issue.hide_connection_error_label()

    def connected(self):
        try:
            self.connection = cx_Oracle.connect(self.url)
            self.database_cursor = self.connection.cursor()
            return True
        except:
            return False
