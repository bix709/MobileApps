# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os
from datetime import datetime
from functools import wraps
from singleton.singleton import Singleton


def date_type(func):
    @wraps(func)
    def wrapped(msg):
        msg = '{date} | {msg_type} : {msg} \n'.format(date=datetime.now(), msg_type=func.__name__.upper(), msg=msg)
        return func(msg)

    return wrapped


class CommonLogger(object):  # TODO
    def __init__(self, **log_files):
        super(CommonLogger, self).__init__()
        self.log_file = log_files.get('log_file')
        self.debug_file = log_files.get('debug_file')

    @date_type
    def info(self, message):
        self.append_to_log(message, True)

    @date_type
    def warn(self, message):
        self.append_to_log(message)

    @date_type
    def error(self, message):
        self.append_to_log(message)

    def append_to_log(self, message, info_only=False):
        if os.path.isfile(self.log_file):
            with open(name=self.log_file, mode='a'):
                self.debug_file.write(message)
                if info_only:
                    self.log_file.write(message)


@Singleton
class DatabaseLogger(CommonLogger):
    def __init__(self, log_file):
        super(CommonLogger, self).__init__(log_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_type, Exception):
            pass
