# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from common_widgets.FittingLabels import CustomLabel, CustomButton


class ConnectionErrorPopup(Popup):
    def __init__(self, error_msg, **kwargs):
        self.title = 'Database connection error'
        self.auto_dismiss = False
        self.error_msg = error_msg
        super(ConnectionErrorPopup, self).__init__(size_hint=(1, 0.1), **kwargs)
        layout = self.create_main_layout()
        self.add_widget(layout)

    def create_main_layout(self):
        layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8))
        layout.add_widget(CustomLabel(text=self.error_msg, text_size=self.size))
        layout.add_widget(CustomButton(text="Exit", text_size=self.size,
                                       on_press=lambda a: self.exit()))
        return layout

    def exit(self):
        App.get_running_app().stop()

    def is_opened(self):
        return True if self._window is not None else False


class ConnectionError(object):
    def __init__(self):
        super(ConnectionError, self).__init__()
        self.current_screen = App.get_running_app().root.current
        self.current_screen_instance = App.get_running_app().root.get_screen(self.current_screen)
        self.connection_error_label = CustomLabel(text="[color=FF0000][b]Connection error."
                                                            "You will be reconnected automatically.[/b][/color]",
                                                  markup=True, size_hint=(1, 0.1), pos=(0, 0))

    def display_connection_error_label(self):
        self.current_screen_instance.add_widget(self.connection_error_label)

    def hide_connection_error_label(self):
        self.current_screen_instance.remove_widget(self.connection_error_label)
