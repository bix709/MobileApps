# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.actionbar import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.carousel import Carousel


class CustomCarousel(Carousel):
    def __init__(self, **kwargs):
        super(CustomCarousel, self).__init__(**kwargs)

    def on_index(self, *args):
        super(CustomCarousel, self).on_index(*args)
        current_tab = str(self.slides.index(self.current_slide))
        self.set_tab_states_to_normal()
        self.get_tab(current_tab).state = 'down'

    def get_tab(self, current_tab):
        return list(filter(lambda a: a.id == current_tab, self.parent.get_action_bar().action_view.children))[0]

    def set_tab_states_to_normal(self):
        for tab in self.parent.get_action_bar().action_view.children:
            tab.state = 'normal'


class CustomActionBar(ActionBar):
    def __init__(self, **kwargs):
        super(CustomActionBar, self).__init__(**kwargs)
        self.add_widget(ActionView())
        self.action_view.add_widget(ActionPrevious())


class CarouselWithActionBar(Screen):
    def __init__(self, **kwargs):
        super(CarouselWithActionBar, self).__init__(**kwargs)
        self.actionBar = CustomActionBar(id='actionBar', background_image='jzielony.png', pos_hint={'x': 0, 'y': 0.92})
        self.carousel = CustomCarousel(id='carousel')
        self.add_widget(self.carousel)
        self.add_widget(self.actionBar)

    def get_action_bar(self):
        return list(filter(lambda a: a.id == 'actionBar', self.children))[0]

    def get_carousel(self):
        return list(filter(lambda a: a.id == 'carousel', self.children))[0]

    def add_screen(self, screen):
        carousel = self.get_carousel()
        index = len(carousel.slides)
        carousel.add_widget(screen)
        button_state = 'down' if index == 0 else 'normal'
        action_bar = self.get_action_bar().action_view
        action_bar.add_widget(ActionSeparator())
        action_bar.add_widget(ActionButton(id=str(index), size_hint=(None, 1), state=button_state,
                                           background_down='b5.png', color=(0, 0, 0, 1), text=screen.name,
                                           on_press=lambda a: carousel.load_slide(carousel.slides[int(a.id)])))
