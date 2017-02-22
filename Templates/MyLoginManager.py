# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from Templates.CalendarScreen import CalendarScreen
from Templates.ChooserPopup import UserChooser
from Templates.DailyScreen import DailyScreen
from Templates.EarningsScreen import EarningsScreen
from Templates.MaintenanceScreen import MaintenanceScreen
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
        if self.logged_user.privileges == "Admin":
            caro.actionBar.action_view.add_widget(UserChooser())
        caro.add_screen(CalendarScreen(background_img='b3.png', name='Calendar'))
        caro.add_screen(DailyScreen(background_img='b4.png', name='DailyScreen'))
        caro.add_screen(TodayScreen(background_img='b5.png', name='Today'))
        caro.add_screen(EarningsScreen(background_img='tlo1.jpg', name='Earnings'))
        caro.add_screen(MaintenanceScreen(background_img='tlo2.jpg', name='Options'))
        self.go_to(caro.name)

    def logout(self):
        super(MyLoginManager, self).logout()
        self.choosen_user = None
        self.get_screen("CarouselWithActionBar").reinitialize()
