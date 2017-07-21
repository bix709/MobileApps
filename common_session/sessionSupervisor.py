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
        super(BackgroundSessionSupervisor, self).__init__()
        self.app_root = app_root
        self.daemon = True

    def run(self):
        wait_until_application_root_initialized(lambda *a, **kw: Clock.schedule_once(self.app_root.correct_login))()


