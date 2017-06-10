# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright: 5517 Company
"""
from kivy.app import App
from kivy.uix.screenmanager import Screen

from adventureskiing.Widgets.DailyScreen import DailyScreen
from common_widgets.Screens import BackgroundAdjustableScreen
from common_widgets.TimeWidgets import CommonCalendar


class CalendarScreen(Screen):
    def __init__(self, calendar_properties, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)
        self.add_widget(MyCalendar(**calendar_properties))

    @property
    def daily_screen(self):
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        return list(filter(lambda a: isinstance(a, DailyScreen), caro.slides))[0]


class MyCalendar(CommonCalendar):
    def on_choose(self, date_button):
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        self.parent.daily_screen.refresh(date_button.id)
        caro.load_slide(caro.slides[int(self.parent.daily_screen.caro_index)])
