# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.clock import Clock

from Templates.db_commands import SqlCommands
from common_callbacks.Callbacks import CommonCallback, wait_for_future_result


class LoginCallback(CommonCallback):
    def __init__(self, *db_args, **db_kwargs):
        super(LoginCallback, self).__init__(*db_args, **db_kwargs)
        self.sql_command = SqlCommands.fetch_logins

    @wait_for_future_result
    def perform_callback(self, *args, **kwargs):  # TODO username, pw , caller as parameters??
        caller = self.get_caller(**kwargs)
        username = kwargs['username']
        password = kwargs['password']
        users_logins = self.database_query.result()
        try:
            Clock.schedule_once(caller.correct_login) if users_logins[username] == str(hash(password)) \
                else Clock.schedule_once(caller.wrong_login)
        except KeyError:
            Clock.schedule_once(caller.wrong_login)
