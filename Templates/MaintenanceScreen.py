# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from common_widgets.CommonPopups import PasswordChanger, UserAddingPopup, UserRemovingPopup, PermissionChanger
from common_widgets.FittingLabels import CustomButton
from common_widgets.Screens import ScrollableScreen


class MaintenanceScreen(ScrollableScreen):
    def __init__(self, **kwargs):
        super(MaintenanceScreen, self).__init__(**kwargs)
        self.main_layout.size_hint_y = 1

    def setup_widgets(self):
        self.main_layout.add_widget(CustomButton(text='Wyloguj',
                                                 on_release=lambda a: App.get_running_app().root.logout()))
        self.main_layout.add_widget(CustomButton(text='Zmien haslo',
                                                 on_release=lambda a: PasswordChanger().open()))
        if App.get_running_app().root.logged_user.privileges == 'Admin':
            self.main_layout.add_widget(CustomButton(text='Dodaj uzytkownika',
                                                     on_release=lambda a: UserAddingPopup().open()))
            self.main_layout.add_widget(CustomButton(text='Usun uzytkownika',
                                                     on_release=lambda a: UserRemovingPopup().open()))
            self.main_layout.add_widget(CustomButton(text='Zmien uprawnienia',
                                                     on_release=lambda a: PermissionChanger().open()))
