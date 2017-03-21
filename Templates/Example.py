# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window
from Templates.MyLoginManager import MyLoginManager


class ExampleApp(App):  # TODO handling int inputs for names etc.
    # TODO przy dodawaniu lekcji, sprawdzanie czy juz nie jest zajeta dana godzina, login isalnum , mozna sie bawic z haslem , znaki specjalne, duze litery itp.
    # TODO export errorcodes , create class performing notification about error
    # TODO export all messages to file with dict ( languages ).
    # TODO better error handling , adding lesson errors, and in option popups.
    # TODO SOMETIMES CONNECTION TO DATABASE FAILS! CHECK THREADS RESPONSIBLE FOR CONNECTION AND LOCKING TASKS.
    # TODO handle whitespaces !!
    def build(self):
        Window.size = (230, 365)
        return MyLoginManager()


if __name__ == '__main__':
    ExampleApp().run()
