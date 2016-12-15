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
        self.text_size = self.width * 2, self.height
        self.valign = 'middle'
        self.halign = 'center'


class FontFittingLabel(Label):
    def __init__(self, **kwargs):
        super(FontFittingLabel, self).__init__(**kwargs)
        self.text_size = self.width * 2, self.height
        self.valign = 'middle'
        self.halign = 'center'
