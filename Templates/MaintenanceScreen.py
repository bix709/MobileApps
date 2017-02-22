# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from common_widgets.CommonPopups import PasswordChanger
from common_widgets.FittingLabels import FontFittingButton
from common_widgets.Screens import ScrollableScreen


class MaintenanceScreen(ScrollableScreen):  # TODO adding / removing user as admin , changing permissions
    def __init__(self, **kwargs):
        super(MaintenanceScreen, self).__init__(**kwargs)

    def setup_widgets(self):
        self.main_layout.add_widget(FontFittingButton(text='Wyloguj',
                                                      on_release=lambda a: App.get_running_app().root.logout()))
        self.main_layout.add_widget(FontFittingButton(text='Zmien haslo',
                                                      on_release=PasswordChanger().open))
        if App.get_running_app().root.logged_user.privileges == 'Admin':
            self.main_layout.add_widget(FontFittingButton(text='Dodaj uzytkownika',
                                                          on_release=UserAddingPopup().open))
            self.main_layout.add_widget(FontFittingButton(text='Usun uzytkownika',
                                                          on_release=UserRemovingPopup().open))
            self.main_layout.add_widget(FontFittingButton(text='Zmien uprawnienia',
                                                          on_release=PermissionChanger().open))
