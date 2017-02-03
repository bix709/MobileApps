# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from Templates.CalendarScreen import CalendarScreen
from Templates.DailyScreen import DailyScreen
from Templates.EarningsScreen import EarningsScreen
from Templates.TodayScreen import TodayScreen
from common_widgets.LoginManager import LoginManager
from common_widgets.TabbedCarousel import CarouselWithActionBar


class MyLoginManager(LoginManager):
    def __init__(self, *args, **kwargs):
        super(MyLoginManager, self).__init__(*args, **kwargs)
        self.choosen_user = None

    def setup_screens(self):
        self.add_widget(CarouselWithActionBar())

    def correct_login(self, *args, **kwargs):
        caro = self.get_screen("CarouselWithActionBar")
        caro.add_screen(CalendarScreen(background_img='tlo2.jpg', name='Calendar'))
        caro.add_screen(DailyScreen(background_img='tlo1.jpg', name='DailyScreen'))
        caro.add_screen(TodayScreen(background_img='tlo2.jpg', name='Today'))
        caro.add_screen(EarningsScreen(background_img='tlo1.jpg', name='Earnings'))
        self.go_to(caro.name)
