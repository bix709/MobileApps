# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App

from AdventureSkiing.Widgets.CalendarScreen import CalendarScreen
from AdventureSkiing.Widgets.DailyScreen import DailyScreen
from AdventureSkiing.Widgets.EarningsScreen import EarningsScreen
from AdventureSkiing.Widgets.TodayScreen import TodayScreen
from AdventureSkiing.Widgets.UserChooser import UserChooser

from AdventureSkiing.Widgets.MaintenanceScreen import MaintenanceScreen
from common_widgets.LoginManager import LoginManager
from common_widgets.TabbedCarousel import CarouselWithActionBar


class MyLoginManager(LoginManager):
    def __init__(self, *args, **kwargs):
        super(MyLoginManager, self).__init__(*args, **kwargs)
        self.choosen_user = None
        self.user_chooser = None

    def setup_screens(self):
        self.add_widget(CarouselWithActionBar())

    def correct_login(self, *args, **kwargs):
        self.setup_carousel_widgets()
        self.go_to("CarouselWithActionBar")

    def setup_carousel_widgets(self):
        caro = self.get_screen("CarouselWithActionBar")
        if self.logged_user.privileges == "Admin":
            self.user_chooser = UserChooser()
            caro.actionBar.action_view.add_widget(self.user_chooser)
        caro.add_screen(CalendarScreen(background_img='{}/graphics/b3.png'.format(App.get_running_app().name), name='Calendar'))
        caro.add_screen(DailyScreen(background_img='{}/graphics/b4.png'.format(App.get_running_app().name), name='DailyScreen'))
        caro.add_screen(TodayScreen(background_img='{}/graphics/b5.png'.format(App.get_running_app().name), name='Today'))
        caro.add_screen(EarningsScreen(background_img='{}/graphics/tlo1.jpg'.format(App.get_running_app().name), name='Earnings'))
        caro.add_screen(MaintenanceScreen(background_img='{}/graphics/tlo2.jpg'.format(App.get_running_app().name), name='Options'))

    def logout(self):
        super(MyLoginManager, self).logout()
        self.choosen_user = None
        self.get_screen("CarouselWithActionBar").reinitialize()

    def refresh_carousel(self):
        caro = self.get_screen("CarouselWithActionBar")
        current_slide_index = caro.carousel.index
        caro.reinitialize()
        self.setup_carousel_widgets()
        caro.carousel.load_slide(caro.carousel.slides[int(current_slide_index)])
