# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright: 5517 Company
"""
from kivy.app import App

from common_widgets.Screens import MyScreen
from common_widgets.TimeWidgets import CommonCalendar


class CalendarScreen(MyScreen):
    def __init__(self, *args, **kwargs):
        super(CalendarScreen, self).__init__(*args, **kwargs)
        self.add_widget(MyCalendar())

    def get_daily_graph_screen(self):
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        return list(filter(lambda a: a.name == "DailyScreen", caro.screens))[0]


class MyCalendar(CommonCalendar):
    def action(self, date_button):
        daily_screen = self.parent.get_daily_graph_screen()
        daily_screen.refresh(date_button.id)
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        caro.load_slide(caro.slides[int(daily_screen.caro_index)])
