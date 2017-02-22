# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from threading import Thread
import sys


class BackgroundCallbackExecutor(Thread):
    def __init__(self, queue):
        """ Waits for sql tasks and executes them in background. """
        super(BackgroundCallbackExecutor, self).__init__()
        self.queue = queue
        self.daemon = True

    def run(self):
        """ Waits for tasks, and executes them sequentially if more than one is enqueued. """
        while True:
            try:
                if self.queue.empty() is False:
                    callback, args, kwargs = self.queue.get()
                    self.queue.unfinished_tasks += 1
                    callback.__call__(args, kwargs)
            except:
                print "Task queue exception {}".format(sys.exc_info()[0])
                self.queue.task_done()
