# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from time import gmtime

from kivy.app import App
from kivy.core.window import Window

from adventureskiing.Database.Callbacks import GetDailyGraph
from adventureskiing.Widgets.LessonsPopup import LessonPopup
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import FontFittingButton
from common_widgets.FittingLabels import FontFittingLabel
from common_widgets.Screens import ScrollableScreen


class DailyScreen(ScrollableScreen):
    def __init__(self, **kwargs):
        self.day = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.busy_buttons_properties = kwargs.pop('busy_buttons_properties', dict())
        self.free_buttons_properties = kwargs.pop('free_buttons_properties', dict())
        self.configuration_buttons_properties = kwargs.pop('configuration_buttons_properties', dict())
        self.header_font_color = kwargs.pop('header_font_color', (1, 1, 1, 1))
        self.buttons_height = Window.height / 7 if Window.height > Window.width else Window.width / 7
        super(DailyScreen, self).__init__(id='DailyScreen', **kwargs)

    def setup_widgets(self):
        user = App.get_running_app().root.choosen_user
        db_kwargs = {'day': self.day, 'user': user}
        schedule_task(callback=GetDailyGraph(**db_kwargs), instance=self)

    def refresh(self, day):
        self.day = day
        self.setup_widgets()

    def add_hours(self, busy_hours):
        self.main_layout.clear_widgets()
        self.setup_option_buttons()
        self.setup_lessons_buttons(busy_hours)

    def setup_lessons_buttons(self, busy_hours):
        for hour in range(9, 21):
            try:
                lesson_info, lesson_id = busy_hours[hour]
                properties = self.busy_buttons_properties
            except KeyError:
                lesson_info = '{}.00 - {}.50'.format(hour, hour)
                lesson_id = "0"
                properties = self.free_buttons_properties
            finally:
                self.main_layout.add_widget(FontFittingButton(text='{}'.format(lesson_info),
                                                              id="{}".format(lesson_id),
                                                              on_press=lambda a: self.show_lesson_details(a),
                                                              size_hint_y=None,
                                                              height=self.buttons_height,
                                                              **properties))

    def setup_option_buttons(self):
        today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.main_layout.add_widget(FontFittingLabel(text='Grafik z dnia {}'.format(self.day), size_hint_y=None,
                                                     height=self.buttons_height,
                                                     color=self.header_font_color))
        self.main_layout.add_widget(FontFittingButton(text='Odśwież', size_hint_y=None,
                                                      height=self.buttons_height,
                                                      on_press=lambda a: self.refresh(self.day),
                                                      **self.configuration_buttons_properties))
        self.main_layout.add_widget(FontFittingButton(text='Pokaz dzisiejszy', size_hint_y=None,
                                                      height=self.buttons_height,
                                                      on_press=lambda a: self.refresh(today),
                                                      **self.configuration_buttons_properties))

    def show_lesson_details(self, button_instance):
        lesson_info = self.get_lesson_info(button_instance)
        LessonPopup(date=self.day, lesson_info=lesson_info).open()

    def get_lesson_info(self, button):
        lesson_info = dict()
        if "#" in button.text:
            lesson_info['ilosc_osob'] = button.text.split("#")[1][0]
            lesson_info['imie'] = button.text.split(",")[0].split("|")[1].strip()
            lesson_info['wiek'] = button.text.split(",")[1].split("lat")[0].strip()
        lesson_info['lesson_id'] = button.id
        lesson_info['hour'] = button.text.split(".")[0]
        return lesson_info
