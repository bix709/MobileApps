# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.actionbar import ActionButton

from common_widgets.FittingLabels import CustomButton


class User(object):
    def __init__(self, user_id, permission, name, lastname):
        self.id = user_id
        self.privileges = permission
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return "#{id} {name} {lastname} ({privileges})".format(**self.__dict__)


class UserButton(CustomButton):
    def __init__(self, user, **kwargs):
        super(UserButton, self).__init__(**kwargs)
        self.user = user


class ActionUserButton(ActionButton, CustomButton):
    def __init__(self, user, **kwargs):
        super(ActionUserButton, self).__init__(**kwargs)
        self.user = user
