# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.label import Label


class WaitingCircle(object):
    def __init__(self, instance):
        self.animation = Label()  # TODO specify label , bg , etc
        self.instance = instance

    def display(self):
        self.instance.add_widget(self.animation)

    def hide(self):
        self.instance.remove_widget(self.animation)
