# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from Templates.Callbacks import UsersToChoose, schedule_task
from Templates.Users import UserButton


class UserChooser(Popup):
    def __init__(self, daily_screen, carousel, date, **kwargs):
        super(UserChooser, self).__init__(title="Wybierz instruktora", size_hint_x=0.75, **kwargs)
        self.daily_screen = daily_screen
        self.caro = carousel
        self.date = date
        self.auto_dismiss = True
        schedule_task(callback=UsersToChoose(), cb_args=tuple(), cb_kwargs={'instance': self})

    def display_users(self, users):
        users_layout = BoxLayout(orientation='vertical')
        for user in users:
            print user
            users_layout.add_widget(UserButton(text=user, user=users[user], on_press=lambda a: self.choosen_graphic(a)))
        self.add_widget(users_layout)

    def choosen_graphic(self, users_button):
        print users_button.user.name
        App.get_running_app().root.choosen_user = users_button.user
        self.dismiss()
        self.daily_screen.refresh(self.date)
        self.caro.load_slide(self.caro.slides[int(self.daily_screen.caro_index)])
