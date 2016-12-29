# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.effects.scroll import ScrollEffect
from kivy.graphics.fbo import Fbo
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from Templates.Callbacks import GetDailyGraph, schedule_task
from Templates.Lessons import LessonPopup
from common_widgets.FittingLabels import FontFittingButton
from common_widgets.FittingLabels import FontFittingLabel
from common_widgets.Screens import MyScreen
from time import gmtime


class DailyScreen(MyScreen):
    def __init__(self, *args, **kwargs):
        super(DailyScreen, self).__init__(size_hint_y=0.9, *args, **kwargs)
        self.day = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.main_layout = GridLayout(cols=1, size_hint_y=None)
        self.main_layout.bind(minimum_height=self.main_layout.setter('height'))
        scroll = ScrollView(size=(Window.width, Window.height * 0.9), size_hint=(1, 1))
        scroll.add_widget(self.main_layout)
        self.add_widget(scroll)
        self.setup_widgets()

    def setup_widgets(self):
        today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.main_layout.add_widget(FontFittingLabel(text='Grafik z dnia {}'.format(self.day), height=45,
                                                     size_hint_y=None))
        self.main_layout.add_widget(FontFittingButton(text='Refresh', height=45, size_hint_y=None,
                                                      on_press=lambda a: self.refresh(self.day)))
        self.main_layout.add_widget(FontFittingButton(text='Pokaz dzisiejszy', height=45, size_hint_y=None,
                                                      on_press=lambda a: self.refresh(today)))
        if App.get_running_app().root.logged_user.privileges == 'Admin':
            self.main_layout.add_widget(FontFittingButton(text='Wyświetl swój\n (obecnie {})'
                                                          .format(App.get_running_app().root.choosen_user.name),
                                                          height=45, size_hint_y=None,
                                                          on_press=lambda a: self.select_yourself()))
        self.get_day_schedule()

    def get_day_schedule(self):
        user = App.get_running_app().root.choosen_user
        db_args = args = ()
        db_kwargs = {'day': self.day, 'user': user}
        kwargs = {'instance': self}
        schedule_task(callback=GetDailyGraph(*db_args, **db_kwargs), cb_args=args, cb_kwargs=kwargs)

    def refresh(self, day):
        self.day = day
        self.main_layout.clear_widgets()
        self.setup_widgets()

    def add_hours(self, busy_hours):
        for hour in range(9, 21):
            try:
                lesson_info, lesson_id = busy_hours[hour]
                color = (1, 0, 0, 1)
            except KeyError:
                lesson_info = '{}.00 - {}.50'.format(hour, hour)
                lesson_id = "0"
                color = (0, 1, 0, 1)
            finally:
                self.main_layout.add_widget(FontFittingButton(text='{}'.format(lesson_info), id="{}".format(lesson_id),
                                                              height=45, on_press=lambda a: self.show_lesson_details(a),
                                                              size_hint_y=None, background_color=color))

    def select_yourself(self):
        App.get_running_app().root.choosen_user = App.get_running_app().root.logged_user
        self.refresh(self.day)

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
