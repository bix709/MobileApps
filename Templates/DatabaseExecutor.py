# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import inspect
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from singleton.singleton import Singleton
import cx_Oracle
import sys

from Templates.ErrorHandlers import *
from Backgrounds import DatabaseTask, execute_in_background
from threading import Thread


class DatabaseConnection(object):
    def __init__(self, url='teter/fx0507@127.0.0.1/Grafiki'):
        super(DatabaseConnection, self).__init__()
        self.url = url
        self.connection = None
        self.database_cursor = None
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

    def connection_error(self, interrupted_func, *args, **kwargs):
        display = ConnectionError()
        display.display_connection_error_label()
        while not self.connected():
            sleep(1)
        interrupted_func(*args, **kwargs)
        display.hide_connection_error_label()

    def connected(self):
        try:
            self.connection = cx_Oracle.connect(self.url)
            self.database_cursor = self.connection.cursor()
            return True
        except:
            return False


class DatabaseExecutor(Thread):
    def __init__(self, queue):
        """ Bag is only for returning database queries to main thread.
        """
        super(DatabaseExecutor, self).__init__()
        self.queue = queue
        self.daemon = True
        self.sql = SqlCommands()

    def run(self):
        while True:
            try:
                if self.queue.empty() is False:
                    task = self.queue.get()
                    self.execute(task)
            except:
                print "Task queue exception {}".format(sys.exc_info()[0])
                self.queue.task_done()

    def execute(self, to_be_executed):
        self.sql.tasks[to_be_executed]()


class SqlCommands(object):
    def __init__(self):
        """Class storing database commands as it's methods. """
        self.tasks = {
            "users_logins": self.fetch_logins
        }

    @execute_in_background
    def fetch_logins(self):
        """ Template method to execute sql commands,
            methods needs to be decorated with @execute_in_background """
        users_logins = {}
        query = DatabaseConnection().fetch_query("select login, password from Instruktorzy")
        if query:
            for result in query:
                users_logins[result[0]] = result[1]
            return {'users_logins': users_logins}
