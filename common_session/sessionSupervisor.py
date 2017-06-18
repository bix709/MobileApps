# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from threading import Thread

from kivy.clock import Clock

from common_utilities.Utilities import wait_until_application_root_initialized


class BackgroundSessionSupervisor(Thread):
    def __init__(self, app_root):
        """ Waits for sql tasks and executes them in background. """
        super(BackgroundSessionSupervisor, self).__init__()
        self.app_root = app_root
        self.daemon = True

    def run(self):
        """ Waits for tasks, and executes them sequentially if more than one is enqueued. """
        wait_until_application_root_initialized(lambda *a, **kw: Clock.schedule_once(self.app_root.correct_login))()


