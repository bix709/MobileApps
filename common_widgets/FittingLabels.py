# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import re

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class CustomButton(Button):
    def __init__(self, text='', **kwargs):
        super(CustomButton, self).__init__(text=App.get_running_app().translator.translate(text), **kwargs)

        self.text_size = self.width * 1.7, self.height
        self.valign = 'middle'
        self.halign = 'center'


class CustomLabel(Label):
    def __init__(self, text='', **kwargs):
        super(CustomLabel, self).__init__(text=App.get_running_app().translator.translate(text), **kwargs)
        self.text_size = self.width * 1.7, self.height
        self.valign = 'middle'
        self.halign = 'center'
