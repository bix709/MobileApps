# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""


class User(object):
    def __init__(self, user_id, permission, name):
        self.id = user_id
        self.permission = permission
        self.name = name
