# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from Templates.TabbedCarousel import *
from kivy.core.window import Window
from Templates.TimeWidgets import *
from Templates.LoginManager import LoginManager
from kivy.config import Config


class ExampleApp(App):
    def build(self):
        Window.size = (230, 365)
        Tested = LoginManager()
        return Tested


if __name__ == '__main__':
    ExampleApp().run()
