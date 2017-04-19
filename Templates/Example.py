# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window
from translate import Translator

from Templates.MyLoginManager import MyLoginManager


class ExampleApp(App):
    # TODO export errorcodes , create class performing notification about error
    # TODO export all messages to file with dict ( languages ).
    # TODO add new feature - setting instructors availability
    def __init__(self, **kwargs):
        super(ExampleApp, self).__init__(**kwargs)
        self.translator = Translator(to_lang='pl')

    def build(self):
        Window.size = (230, 365)
        return MyLoginManager()


if __name__ == '__main__':
    ExampleApp().run()
