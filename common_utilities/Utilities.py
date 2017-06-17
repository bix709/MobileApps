# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from contextlib import contextmanager

import time


@contextmanager
def ignored(exc):
    try:
        yield
    except exc:
        pass


def call_once_within_period(period_in_seconds):
    class call_once_within_time(object):
        def __init__(self, func):
            self.time = 0
            self.func = func

        def __call__(self, *args):
            if time.time() > self.time + period_in_seconds:
                self.time = time.time()
                return self.func(*args)
    return call_once_within_time
