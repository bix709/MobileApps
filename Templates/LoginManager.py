# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from kivy.uix.screenmanager import ScreenManager
from Templates.CommonWidgets import MyScreen, LoginScreen
from kivy.uix.screenmanager import FadeTransition
from Templates.DatabaseExecutor import SqlCommandsExecutor


class LoginManager(ScreenManager):
    def __init__(self, **kwargs):
        super(LoginManager, self).__init__(**kwargs)
        self.id = "LoginManager"
        self.bag = {}
        self.transition = FadeTransition()
        self.add_widget(LoginScreen(background_img='tlo2.jpg'))
        self.add_widget(MyScreen(background_img='tlo2.jpg', name='First Screen'))
        self.database_executor = SqlCommandsExecutor(self.bag)
        self.database_executor.fetch_logins()

    def handle_login(self, username, password):
        users_logins = self.get_from_bag('users_logins')
        try:
            self.correct_login() if users_logins[username] == str(hash(password)) else self.wrong_login()
        except KeyError:
            self.wrong_login()

    def get_from_bag(self, item):
        try:
            return self.bag[item]
        except KeyError:
            print 'Cant connect / read logins from database.'

    def correct_login(self):
        self.database_executor.fetch_logins()
        self.current = "First Screen"

    def wrong_login(self):
        self.get_login_screen().wrong_login_attempt()

    def get_login_screen(self):
        return list(filter(lambda a: a.name == 'Login Screen', self.children))[0]
