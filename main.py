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
    # TODO dailsyscreen stays on previous day when after 0.00 (probably to 1:00 ) - check time
    # TODO refactoring - no communication via returning none, true, false in db_commands. do it via exceptions.
    # TODO Changing state of already down action button on click
    # TODO remember session - logged in users after restart app
    # TODO refactoring - private methods
    # TODO add refreshing on resume, refreshing userchooser, and whole carousel ( if permissions changed, or user removed)
    # TODO automatically logout removed users
    # TODO add closing keyboard on confirmations in popup
    #
    # TODO add session on login ,remove on logout, and on user removal
    # TODO checking if session didnt expire !!!!
    # TODO refresh on userchooser's change user
    # TODO create common app, common session, and custom session with overriden sql command


    # TODO Needed fixes : userchooser when automatic logging, supervisor needs to check session freshness, and stops gracefully on logout.
    # TODO fix error handling when no connection to db
    # TODO Reconsider using singleton in notification listener, session supervisor, background callback executioner
    # TODO if working, cleanup after redundant service
    # TODO remove redundant logic in executing callbacks ( probably no need for doing it on threads), change to sequential
    # TODO refactoring - notification manager must be importing accoring to platform, remove ignoring import exception in myloginmanager
    icon = 'adventureskiing/graphics/logo.png'

    def build(self):
        Window.bind(on_keyboard=self.handle_go_back_button)
        Window.icon = 'adventureskiing/graphics/logo.png'
        return MyLoginManager()

    def on_pause(self):
        return True

    def handle_go_back_button(self, window, keycode1, keycode2, text, modifiers):
        return self.root.go_back() if keycode1 in [27, 1001] else False


if __name__ == '__main__':
    AdventureSkiing().run()
