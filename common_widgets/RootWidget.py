# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from Queue import Queue
from common_callbacks.CallbackExecutor import BackgroundCallbackExecutor


class RootWidget(object):
    def __init__(self):
        super(RootWidget, self).__init__()
        self.task_queue = Queue(maxsize=0)
        BackgroundCallbackExecutor(self.task_queue).start()
