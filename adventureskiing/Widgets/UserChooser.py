# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.uix.actionbar import ActionGroup

from adventureskiing.Database.Callbacks import UsersToChoose
from adventureskiing.Database.MySQL.db_commands import SqlCommands
from common_callbacks.Callbacks import schedule_task
from adventureskiing.Utils.Users import ActionUserButton


class UserChooser(ActionGroup):  # TODO fix size issues ( not opening spinner ) and resizing exception issue, close dropdown!
    def __init__(self, **kwargs):
        super(UserChooser, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        # self.size = (100, 20)
        self.text = App.get_running_app().root.logged_user.name
        self.mode = 'spinner'
        self.fetch_users()

    def fetch_users(self):
        """ Cannot be a background task, to set it in action view properly!! """
        self.assign_users(SqlCommands.get_all_users())

    def assign_users(self, users):
        for user in users:
            if user is not None:
                self.add_widget(ActionUserButton(text=user, user=users[user],
                                                 on_release=lambda a: self.choose_user(a.user)))

    def choose_user(self, user):
        App.get_running_app().root.choosen_user = user
        self.text = user.name
