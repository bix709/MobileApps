# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from contextlib import contextmanager


@contextmanager
def ignored(exc):
    try:
        yield
    except exc:
        pass
