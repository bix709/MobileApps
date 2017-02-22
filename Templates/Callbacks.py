# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.clock import Clock

from Templates.Users import User
from Templates.db_commands import SqlCommands
from common_callbacks.Callbacks import CommonCallback, wait_for_future_result, schedule_task


class LoginCallback(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.fetch_logins

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        if App.get_running_app().root.logged_user is None:
            try:
                imie, id, uprawnienia = self.database_query.result()
                App.get_running_app().root.logged_user = User(name=imie, user_id=id, permission=uprawnienia)
                App.get_running_app().root.choosen_user = App.get_running_app().root.logged_user
                Clock.schedule_once(instance.correct_login)
            except:
                Clock.schedule_once(instance.wrong_login)


class GetDailyGraph(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.get_daily_graph

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        Clock.schedule_once(lambda a: self.set_hours(instance))

    def set_hours(self, instance):
        busy_hours = self.database_query.result()
        instance.add_hours(busy_hours)


class UsersToChoose(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.get_all_users

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        Clock.schedule_once(lambda a: self.set_users(instance))

    def set_users(self, instance):
        users = self.database_query.result()
        instance.assign_users(users)


class InsertNewLesson(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.insert_new_lesson

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        Clock.schedule_once(instance.on_successful_execution)


class RemoveLesson(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.remove_lesson

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        Clock.schedule_once(instance.on_successful_execution)


class GetUnoccupied(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.get_unoccupied

    @wait_for_future_result
    def perform_callback(self, instance, button_instance, *args, **kwargs):
        Clock.schedule_once(lambda a: self.set_unoccupied(instance, button_instance))

    def set_unoccupied(self, instance, button_instance):
        unoccupied_instructors = self.database_query.result()
        instance.set_unoccupied(unoccupied_instructors, button_instance)


class GetEarnings(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.get_earnings

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        Clock.schedule_once(lambda a: self.show_earnings(instance))

    def show_earnings(self, instance):
        instance.show_earnings(self.database_query.result())


class PasswordChange(CommonCallback):
    @property
    def sql_command(self):
        return SqlCommands.password_update

    @wait_for_future_result
    def perform_callback(self, instance, *args, **kwargs):
        func = instance.on_successful_change() if self.database_query.result() is True else instance.on_wrong_attempt()
        Clock.schedule_once(func)
