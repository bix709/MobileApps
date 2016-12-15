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
    def __init__(self, **kwargs):
        """ This widget is supposed to be root of application!
            Remember to perform GUI move first (with old data) , then callback. """
        super(LoginManager, self).__init__(id="LoginManager", transition=FadeTransition(), **kwargs)
        self.task_queue = Queue(maxsize=0)
        self.add_widget(LoginScreen(background_img='tlo2.jpg'))
        self.setup_screens()
        BackgroundCallbackExecutor(self.task_queue).start()

    def setup_screens(self):
        self.add_widget(MyScreen(background_img='tlo2.jpg', name='First Screen'))

    def handle_login(self, username, password):
        args = db_args = ()
        db_kwargs = {}
        print self.task_queue.unfinished_tasks
        kwargs = {'username': username, 'password': password, 'instance': self}
        self.task_queue.put((LoginCallback(db_args, db_kwargs), args, kwargs))

    def correct_login(self, *args, **kwargs):
        self.go_to("First Screen")

    def wrong_login(self, *args, **kwargs):
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
