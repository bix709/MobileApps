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
from common_widgets.Screens import MyScreen, LoginScreen


class LoginManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        """ This widget is supposed to be root of application!
            Remember to perform GUI move first (with old data) , then callback. """
        super(LoginManager, self).__init__(id="LoginManager", transition=FadeTransition(), **kwargs)
        self.task_queue = Queue(maxsize=0)
        self.add_widget(LoginScreen(background_img='tlo2.jpg'))
        self.setup_screens()
        BackgroundCallbackExecutor(self.task_queue).start()

    def setup_screens(self):
        """ Override this method to set up screens to be displayed after correct_login. """
        self.add_widget(MyScreen(background_img='tlo2.jpg', name='First Screen'))

    def handle_login(self, username, password):
        args = db_args = ()
        db_kwargs = {}
        kwargs = {'username': username, 'password': password, 'instance': self}
        self.task_queue.put((LoginCallback(db_args, db_kwargs), args, kwargs))

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
