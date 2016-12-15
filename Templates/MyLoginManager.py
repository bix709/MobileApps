# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from common_widgets.LoginManager import LoginManager
from common_widgets.Screens import MyScreen
from common_widgets.TabbedCarousel import CarouselWithActionBar


class MyLoginManager(LoginManager):
    def __init__(self, *args, **kwargs):
        super(MyLoginManager, self).__init__(*args, **kwargs)

    def setup_screens(self):
        self.add_widget(CarouselWithActionBar())

    def correct_login(self, *args, **kwargs):
        caro = self.get_screen("CarouselWithActionBar")
        caro.add_screen(MyScreen(background_img='tlo2.jpg', name='First screen'))
        caro.add_screen(MyScreen(background_img='tlo1.jpg', name='Second screen'))
        self.go_to(caro.name)
