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
    def wrapped(*args, **kwargs):
        caller = args[0].get_caller(**kwargs)
        # wait_animation = WaitingCircle(caller)
        # wait_animation.display()
        caller.task_queue.join()
        # wait_animation.hide()
        return function(*args, **kwargs)

    return wrapped


class CommonCallback(object):
    """ Abstract class (template) for callbacks """

    def __init__(self, *database_args, **database_kwargs):
        """ Attribute sql_command should be set by overriding constructor. """
        self.database_args = database_args
        self.database_kwargs = database_kwargs
        self.sql_command = None
        super(CommonCallback, self).__init__()

    def __call__(self, args, kwargs):
        """ Override this method only if you know what you're doing! """
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.perform_callback, *args, **kwargs)
            self.database_query = executor.submit(self.sql_command, *self.database_args, **self.database_kwargs)

    def get_caller(self, **kwargs):
        """ Returns caller's screen. """
        try:
            return kwargs['instance']
        except KeyError:
            print 'No instance given to callback'

    @wait_for_future_result
    def perform_callback(self):
        """ You need to override this method.
            It's executed after result from database query is obtained.
            It must be decorated with @wait_for_future_result.
            Remember to perform caller's methods using Clock.schedule.
        """
        pass
