# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright: 5517 Company
"""
from kivy.app import App
from common_widgets.Screens import BackgroundAdjustableScreen
from common_widgets.TimeWidgets import CommonCalendar


class CalendarScreen(BackgroundAdjustableScreen):
    def __init__(self, *args, **kwargs):
        super(CalendarScreen, self).__init__(*args, **kwargs)
        self.add_widget(MyCalendar())

    @property
    def daily_screen(self):
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        return list(filter(lambda a: a.name == "DailyScreen", caro.slides))[0]


class MyCalendar(CommonCalendar):
    def on_choose(self, date_button):
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        self.parent.daily_screen.refresh(date_button.id)
        caro.load_slide(caro.slides[int(self.parent.daily_screen.caro_index)])
