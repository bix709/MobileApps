# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import time
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from Templates.Callbacks import GetUnoccupied
from Templates.DailyScreen import DailyScreen
from Templates.Lessons import LessonPopup
from Templates.Users import UserButton
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import CustomButton
from common_widgets.Screens import CustomScreen, ScrollableScreen
from time import gmtime


class TodayScreen(ScrollableScreen):
    def __init__(self, **kwargs):
        self.unoccupied_users = DropDown()
        self.today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        super(TodayScreen, self).__init__(**kwargs)

    def setup_widgets(self):
        for hour in range(9, 21):
            if hour > time.gmtime().tm_hour:
                self.main_layout.add_widget(CustomButton(text="{}.00 - {}.50".format(hour, hour),
                                                         id="{}".format(hour),
                                                         size_hint_y=None, height=45,
                                                         on_press=lambda a: self.display_unoccupied(a)))

    def display_unoccupied(self, instance):
        db_kwargs = {
            'date': self.today,
            'hour': instance.id
        }
        schedule_task(callback=GetUnoccupied(**db_kwargs), cb_args=tuple(), cb_kwargs={'instance': self,
                                                                                       'button_instance': instance})

    def set_unoccupied(self, unoccupied_instructors, instance):
        self.unoccupied_users.dismiss()
        self.unoccupied_users.clear_widgets()
        if unoccupied_instructors is not None:
            for instructor in unoccupied_instructors:
                self.unoccupied_users.add_widget(UserButton(text="{}".format(instructor.name), user=instructor,
                                                            size_hint_y=None, height=40,
                                                            on_press=lambda a: self.add_lesson(a, instance)))
            self.unoccupied_users.open(instance)

    def add_lesson(self, instance, button):
        App.get_running_app().root.choosen_user = instance.user
        lesson_info = dict()
        lesson_info['lesson_id'] = "0"
        lesson_info['hour'] = button.text.split(".")[0]
        LessonPopup(date=self.today, lesson_info=lesson_info).open()
