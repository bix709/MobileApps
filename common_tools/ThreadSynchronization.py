# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App


def mark_task_as_done(function):
    """ Sets all tasks as done ( before next callback queue.unfinished_tasks must be incremented ). """

    def wrapped(*args, **kwargs):
        future = function(*args, **kwargs)
        unfinished = App.get_running_app().root.task_queue.unfinished_tasks
        for i in range(0, unfinished):
            App.get_running_app().root.task_queue.task_done()
        return future

    return wrapped
