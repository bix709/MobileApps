# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window
from Templates.MyLoginManager import MyLoginManager


class ExampleApp(App):
    def build(self):
        Window.size = (230, 365)
        return MyLoginManager()


if __name__ == '__main__':
    ExampleApp().run()
