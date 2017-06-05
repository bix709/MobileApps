# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.button import Button
from kivy.uix.label import Label


class FontFittingButton(Button):
    def __init__(self, **kwargs):
        super(FontFittingButton, self).__init__(**kwargs)
        self.valign = 'middle'
        self.halign = 'center'
        self.bind(size=self.set_text_size)

    def set_text_size(self, *args, **kwargs):
        self.text_size = self.size


class FontFittingLabel(Label):
    def __init__(self, **kwargs):
        super(FontFittingLabel, self).__init__(**kwargs)
        self.valign = 'middle'
        self.halign = 'center'
        self.bind(size=self.set_text_size)

    def set_text_size(self, *args, **kwargs):
        self.text_size = self.size
