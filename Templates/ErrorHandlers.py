# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import sys
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from Templates.CommonWidgets import FontFittingLabel, FontFittingButton


def handle_connection_errors(function):
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            args[0].connection_error()

    return wrapped


class ConnectionErrorPopup(Popup):
    def __init__(self, error_msg, **kwargs):
        self.title = 'Database connection error'
        self.error_msg = error_msg
        super(ConnectionErrorPopup, self).__init__(**kwargs)
        layout = self.create_main_layout()
        self.add_widget(layout)

    def create_main_layout(self):
        layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8))
        layout.add_widget(FontFittingLabel(text=self.error_msg, text_size=self.size))
        layout.add_widget(FontFittingButton(text="Try to reconnect", text_size=self.size,
                                            on_press=lambda a: self.reconnect()))
        return layout

    def reconnect(self):
        print 'reconnect'
