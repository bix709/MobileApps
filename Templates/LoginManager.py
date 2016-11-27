# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from kivy.uix.screenmanager import ScreenManager
from Templates.CommonWidgets import MyScreen, LoginScreen
from kivy.uix.screenmanager import FadeTransition
from Templates.DatabaseExecutor import DatabaseExecutor
from time import sleep
from Queue import Queue


class LoginManager(ScreenManager):
    def __init__(self, **kwargs):
        """ This widget is supposed to be root of application! """
        super(LoginManager, self).__init__(id="LoginManager", transition=FadeTransition(), **kwargs)
        self.bag = dict()
        self.task_queue = Queue(maxsize=0)
        self.add_widget(LoginScreen(background_img='tlo2.jpg'))
        self.setup_screens()
        DatabaseExecutor(self.task_queue).start()
        self.task_queue.put("users_logins")

    def setup_screens(self):
        self.add_widget(MyScreen(background_img='tlo2.jpg', name='First Screen'))

    def handle_login(self, username, password):
        users_logins = self.get_from_bag("users_logins")
        try:
            self.correct_login() if users_logins[username] == str(hash(password)) else self.wrong_login()
        except KeyError:
            self.wrong_login()

    def get_from_bag(self, item):
        """Freezes GUI and waits for fetch finished."""
        try:
            self.task_queue.join()  # TODO koleczko czekania
            return self.bag[item]
        except:
            print "Error no such item in root bag."

    def correct_login(self):
        self.go_to("First Screen")

    def wrong_login(self):
        try:
            self.get_screen("Login Screen").wrong_login_attempt()
        except:
            print "No such screen"

    def go_to(self, name):
        self.current = name
        # screen = self.get_screen(name)
        # self.current = screen.name
        # screen.assume_not_fetched()
        # screen.fetch_prequisites()
        # TODO wait for fetch ( get from bag )
        # screen.bind_widgets() # Show hidden
