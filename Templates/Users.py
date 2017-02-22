# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.actionbar import ActionButton

from common_widgets.FittingLabels import FontFittingButton


class User(object):
    def __init__(self, user_id, permission, name):
        self.id = user_id
        self.privileges = permission
        self.name = name

    def __str__(self):
        return "User {name}, with id {id}, has permissions {permissions}".format(name=self.name,
                                                                                 id=self.id,
                                                                                 permissions=self.privileges)


class UserButton(FontFittingButton):
    def __init__(self, user, **kwargs):
        super(UserButton, self).__init__(**kwargs)
        self.user = user


class ActionUserButton(ActionButton, FontFittingButton):
    def __init__(self, user, **kwargs):
        super(ActionUserButton, self).__init__(**kwargs)
        self.user = user
