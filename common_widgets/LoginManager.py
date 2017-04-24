# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from Queue import Queue

from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import ScreenManager

from Templates.Callbacks import LoginCallback
from common_callbacks.CallbackExecutor import BackgroundCallbackExecutor
from common_callbacks.Callbacks import schedule_task
from common_widgets.RootWidget import RootWidget
from common_widgets.Screens import BackgroundAdjustableScreen, LoginScreen


class LoginManager(ScreenManager, RootWidget):
    def __init__(self, *args, **kwargs):
        """ This widget is supposed to be root of application! """
        super(LoginManager, self).__init__(id="LoginManager", transition=FadeTransition(), **kwargs)
        self.logged_user = None
        self.add_widget(LoginScreen(background_img='../graphics/tlo2.jpg'))
        self.setup_screens()

    def setup_screens(self):
        """ Override this method to set up screens to be displayed after correct_login. """
        self.add_widget(BackgroundAdjustableScreen(background_img='../graphics/tlo2.jpg', name='First Screen'))

    def handle_login(self, username, password):
        args = db_args = ()
        db_kwargs = {'username': username, 'password': password}
        kwargs = {'instance': self}
        schedule_task(callback=LoginCallback(*db_args, **db_kwargs), cb_args=args, cb_kwargs=kwargs)

    def correct_login(self, *args, **kwargs):
        """ Override this method to navigate to first widget after successfull login. """
        screen = self.get_screen("First Screen")
        self.go_to(screen.name)

    def wrong_login(self, *args, **kwargs):
        try:
            self.get_screen("Login Screen").wrong_login_attempt()
        except:
            print "Wrong Login Screen attached."

    def go_to(self, name):
        self.current = name

    def logout(self):
        self.logged_user = None
        self.clear_widgets()
        self.setup_screens()
        self.get_screen('Login Screen').reinitialize()
        self.go_to('Login Screen')
