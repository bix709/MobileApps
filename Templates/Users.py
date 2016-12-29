# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from common_widgets.FittingLabels import FontFittingButton


class User(object):
    def __init__(self, user_id, permission, name):
        self.id = user_id
        self.privileges = permission
        self.name = name


class UserButton(FontFittingButton):
    def __init__(self, user, **kwargs):
        super(UserButton, self).__init__(**kwargs)
        self.user = user
