# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from threading import *


class DatabaseTask(Thread):
    def __init__(self, function, *args, **kwargs):
        super(DatabaseTask, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.args[0].bag.update(self.function(self.args[0]))
