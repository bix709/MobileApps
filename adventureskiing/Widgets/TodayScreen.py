# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import time
from time import gmtime

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown

from adventureskiing.Database.Callbacks import GetUnoccupied
from adventureskiing.Utils.Users import UserButton
from adventureskiing.Widgets.LessonsPopup import LessonPopup
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import FontFittingButton
from common_widgets.Screens import ScrollableScreen


class TodayScreen(ScrollableScreen):
    def __init__(self, **kwargs):
        self.unoccupied_users = DropDown()
        self.today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.button_properties = kwargs.pop('buttons_properties', dict())
        self.busy_buttons_background = kwargs.pop('busy_buttons_background', '')
        self.dropdown_buttons_properties = kwargs.pop('dropdown_buttons_properties', dict())
        self.dropdown_height = Window.height / 7 if Window.height > Window.width else Window.width / 7
        super(TodayScreen, self).__init__(**kwargs)

    def setup_widgets(self):
        for hour in range(9, 21):
            if hour > time.gmtime().tm_hour:
                self.main_layout.add_widget(FontFittingButton(text="{}.00 - {}.50".format(hour, hour),
                                                              id="{}".format(hour), size_hint_y=None,
                                                              height=self.dropdown_height,
                                                              on_press=lambda a: self.display_unoccupied(a),
                                                              **self.button_properties))

    def display_unoccupied(self, instance):
        db_kwargs = {
            'date': self.today,
            'hour': instance.id
        }
        schedule_task(callback=GetUnoccupied(**db_kwargs), instance=self, button_instance=instance)

    def set_unoccupied(self, unoccupied_instructors, instance):
        self.unoccupied_users.clear_widgets()
        if unoccupied_instructors:
            instance.background_normal = self.button_properties['background_normal']
            for instructor in unoccupied_instructors:
                self.unoccupied_users.add_widget(UserButton(text="{}".format(instructor.name), user=instructor,
                                                            size_hint_y=None,
                                                            height=self.dropdown_height/1.5,
                                                            on_press=lambda a: self.add_lesson(a, instance),
                                                            **self.dropdown_buttons_properties))
            self.unoccupied_users.open(instance)
        else: instance.background_normal = self.busy_buttons_background

    def add_lesson(self, instance, button):
        self.unoccupied_users.dismiss()
        App.get_running_app().root.choosen_user = instance.user
        lesson_info = dict()
        lesson_info['lesson_id'] = "0"
        lesson_info['hour'] = button.text.split(".")[0]
        LessonPopup(date=self.today, lesson_info=lesson_info).open()
