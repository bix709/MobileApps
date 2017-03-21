# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from concurrent.futures import ThreadPoolExecutor
from functools import wraps

from kivy.app import App


def wait_for_future_result(function):
    @wraps(function)
    def wrapped(*args, **kwargs):  # TODO animation circle
        caller = App.get_running_app().root
        # wait_animation = WaitingCircle(caller)
        # wait_animation.display()
        caller.task_queue.join()
        # wait_animation.hide()
        return function(*args, **kwargs)

    return wrapped


def schedule_task(callback, cb_args, cb_kwargs):
    App.get_running_app().root.task_queue.put((callback, cb_args, cb_kwargs))


class CommonCallback(object):
    """ Abstract class (template) for callbacks """

    def __init__(self, *database_args, **database_kwargs):
        """ Attribute sql_command should be set by overriding constructor. """
        self.database_args = database_args
        self.database_kwargs = database_kwargs
        super(CommonCallback, self).__init__()

    def __call__(self, args, kwargs):
        """ Override this method only if you know what you're doing! """
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.perform_callback, *args, **kwargs)
            self.database_query = executor.submit(self.sql_command, *self.database_args, **self.database_kwargs)

    def get_caller(self, **kwargs):
        """ Returns caller's screen. """
        return kwargs.get('instance')

    @property
    def sql_command(self):
        """
        Override this method to set sql command to be executed with callback.
        Must be decorated with @property
        :return: reference to SQL Command ( callable one ).
        """
        return lambda a: 1

    @wait_for_future_result
    def perform_callback(self, *args, **kwargs):
        """ You need to override this method.
            It's executed after result from database query is obtained.
            It must be decorated with @wait_for_future_result.
            Remember to perform caller's methods using Clock.schedule.
        """
        pass
