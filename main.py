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
    # TODO add new feature - editing existing lesson
    # TODO unit tests
    # TODO font sizes - bind to button size
    # TODO refactoring - remove redundant IFs in db_commands, remove  redundant iterations , when casting to tuples/lists
    # TODO dailsyscreen stays on previous day when after 0.00 (probably to 1:00 ) - check time
    # TODO zmiana hasla wywala apke !
    # TODO refactoring - no communication via returning none, true, false in db_commands. do it via exceptions.
    icon = 'adventureskiing/graphics/logo.png'

    def build(self):
        Window.size = (250, 450)
        Window.icon = 'adventureskiing/graphics/logo.png'
        return MyLoginManager()

if __name__ == '__main__':
    AdventureSkiing().run()
