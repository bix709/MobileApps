# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.core.window import Window
from kivy.uix.actionbar import ActionSeparator

from adventureskiing.Config.Widgets_properties import *
from adventureskiing.Widgets.CalendarScreen import CalendarScreen
from adventureskiing.Widgets.DailyScreen import DailyScreen
from adventureskiing.Widgets.EarningsScreen import EarningsScreen
from adventureskiing.Widgets.TodayScreen import TodayScreen
from adventureskiing.Widgets.UserChooser import UserChooser

from adventureskiing.Widgets.MaintenanceScreen import MaintenanceScreen
from common_widgets.LoginManager import LoginManager
from common_widgets.TabbedCarousel import CarouselWithActionBar


class MyLoginManager(LoginManager):
    def __init__(self, *args, **kwargs):
        super(MyLoginManager, self).__init__(loginscreen_properties=loginscreen_properties,
                                             loginbutton_properties=loginbutton_properties,
                                             credential_label_properties=credential_label_properties,
                                             *args, **kwargs)
        self.choosen_user = None
        self.user_chooser = None

    def setup_screens(self):
        self.add_widget(CarouselWithActionBar(**carousel_with_actionbar_properties))

    def correct_login(self, *args, **kwargs):
        self.setup_carousel_widgets()
        self.go_to("CarouselWithActionBar")

    def setup_carousel_widgets(self):
        caro = self.get_screen("CarouselWithActionBar")
        self.setup_carousels_screens(caro)
        if self.logged_user.privileges == "Admin":
            self.setup_user_chooser(caro)

    def setup_carousels_screens(self, caro):
        caro.add_screen(CalendarScreen(**calendarscreen_properties))
        caro.add_screen(DailyScreen(**dailyscreen_properties))
        caro.add_screen(TodayScreen(**todayscreen_properties))
        caro.add_screen(EarningsScreen(**earningscreen_properties))
        caro.add_screen(MaintenanceScreen(**maintenancescreen_properties))

    def setup_user_chooser(self, caro):
        self.user_chooser = UserChooser(**user_chooser_properties)
        caro.actionBar.action_view.add_widget(ActionSeparator(**separators_properties))
        caro.actionBar.action_view.add_widget(self.user_chooser)
        caro.actionBar.action_view._layout_all()

    def logout(self, *args, **kwargs):
        super(MyLoginManager, self).logout()
        self.choosen_user = None
        self.get_screen("CarouselWithActionBar").reinitialize()

    def refresh_carousel(self):
        caro = self.get_screen("CarouselWithActionBar")
        current_slide_index = caro.carousel.index
        caro.reinitialize()
        self.setup_carousel_widgets()
        caro.carousel.load_slide(caro.carousel.slides[int(current_slide_index)])
