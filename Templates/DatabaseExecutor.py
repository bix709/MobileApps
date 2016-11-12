# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

import cx_Oracle


class DatabaseConnection(object):
    def __init__(self, url='teter/fx0507@127.0.0.1/Grafiki'):
        super(DatabaseConnection, self).__init__()
        self.url = url
        self.connection = cx_Oracle.connect(self.url)
        self.database_cursor = self.connection.cursor()

    def fetch_query(self, sql_command):
        try:
            query = self.database_cursor.execute(sql_command)
            return query
        except:
            print 'Database query fetcher error.'

    def execute_command(self, sql_command):
        try:
            self.database_cursor.execute(sql_command)
            self.connection.commit()
        except:
            print 'Database command executor error.'


class SqlCommandsExecutor(object):
    def __init__(self):
        super(SqlCommandsExecutor, self).__init__()
        self.database = DatabaseConnection()

    def fetch_logins(self):
        users_logins = {}
        query = self.database.fetch_query("select login, password from Instruktorzy")
        for result in query:
            users_logins[result[0]] = result[1]
        return {'users_logins': users_logins}
