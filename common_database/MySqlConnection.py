# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from time import sleep
import mysql.connector
from adventureskiing.Database.db_config.config import mysql_config as db_config
from common_database.ErrorHandlers import *


class DatabaseConnection(object):
    def __init__(self):
        super(DatabaseConnection, self).__init__()
        self.connection = None
        self.database_cursor = self.connect_to_database()

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(**db_config)
            return self.connection.cursor()
        except:
            self.connection_error()

    def fetch_query(self, sql_command):
        self.database_cursor.execute(sql_command)
        return self.database_cursor.fetchall()

    def execute_command(self, sql_command):
        self.database_cursor.execute(sql_command)
        self.connection.commit()

    def connection_error(self):
        connection_error = ConnectionError()
        connection_error.display_error()
        while not self.connected():
            sleep(1)
        connection_error.hide_error()

    def connected(self):
        try:
            self.connection = mysql.connector.connect(**db_config)
            self.database_cursor = self.connection.cursor()
            return True
        except:
            return False

    def __del__(self):
        self.database_cursor.close()
        self.connection.close()
