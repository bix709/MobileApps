# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager

from adventureskiing.Database.Callbacks import LoginCallback
from common_callbacks.Callbacks import schedule_task
from common_widgets.RootWidget import RootWidget
from common_widgets.Screens import LoginScreen


class LoginManager(ScreenManager, RootWidget):
    def __init__(self, loginbutton_properties, credential_label_properties, loginscreen_properties, *args, **kwargs):
        """ This widget is supposed to be root of application! """
        self.size = Window.size
        self.login_screen = LoginScreen(loginbutton_properties=loginbutton_properties,
                                        credential_label_properties=credential_label_properties,
                                        **loginscreen_properties)
        super(LoginManager, self).__init__(id="LoginManager", transition=FadeTransition(), **kwargs)
        self.logged_user = None
        self.setup_screens()

    def setup_screens(self):
        """ Override this method to set up screens to be displayed after correct_login. """
        self.add_widget(self.login_screen)

    def handle_login(self, username, password):
        db_kwargs = {'username': username, 'password': password}
        schedule_task(callback=LoginCallback(**db_kwargs), instance=self)

    def correct_login(self, *args, **kwargs):
        """ Override this method to navigate to first widget after successfull login. """
        screen = self.get_screen("First Screen")
        self.go_to(screen.name)

    def wrong_login(self, *args, **kwargs):
        self.login_screen.wrong_login_attempt()

    def go_to(self, name):
        self.current = name

    def logout(self, *args, **kwargs):
        self.logged_user = None
        self.clear_widgets()
        self.login_screen.reinitialize()
        self.setup_screens()
        self.go_to(self.login_screen.name)
