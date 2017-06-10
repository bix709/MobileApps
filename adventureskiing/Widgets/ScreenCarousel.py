# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from common_widgets.TabbedCarousel import CarouselWithActionBar


class ScreenCarousel(CarouselWithActionBar):

    def get_proper_background_image(self):
        return self.background_img

