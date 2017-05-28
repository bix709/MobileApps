# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window

from adventureskiing.Widgets.MyLoginManager import MyLoginManager


class AdventureSkiing(App):
    # TODO export errorcodes , create class performing notification about error
    # TODO export all messages to file with dict ( languages ).
    # TODO add new feature - setting instructors availability
    def build(self):
        return MyLoginManager()


if __name__ == '__main__':
    AdventureSkiing().run()
