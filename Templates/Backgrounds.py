# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from threading import *
from kivy.app import App


def execute_in_background(function):
    def wrapped(*args, **kwargs):
        DatabaseTask(function, *args, **kwargs).start()

    return wrapped


class DatabaseTask(Thread):
    def __init__(self, function, *args, **kwargs):
        super(DatabaseTask, self).__init__()
        self.daemon = True
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        future = self.function(*self.args, **self.kwargs)
        App.get_running_app().root.bag.update(future)
        App.get_running_app().root.task_queue.task_done()
