# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.clock import Clock

from Templates.Users import User
from Templates.db_commands import SqlCommands
from common_callbacks.Callbacks import CommonCallback, wait_for_future_result


class LoginCallback(CommonCallback):
    @property
    def get_sql_command(self):
        return SqlCommands.fetch_logins

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        try:
            imie, id, uprawnienia = self.database_query.result()
            App.get_running_app().root.logged_user = User(name=imie, user_id=id, permission=uprawnienia)
            App.get_running_app().root.chosen_user = App.get_running_app().root.logged_user
            Clock.schedule_once(instance.correct_login)
        except:
            Clock.schedule_once(instance.wrong_login)


class GetDailyGraph(CommonCallback):
    @property
    def get_sql_command(self):
        return SqlCommands.get_daily_graph

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        Clock.schedule_once(lambda a: self.set_hours(instance))

    def set_hours(self, instance):
        busy_hours = self.database_query.result()
        instance.add_hours(busy_hours)
