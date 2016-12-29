# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.graphics.fbo import Fbo
from kivy.uix.actionbar import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.carousel import Carousel


class CustomCarousel(Carousel):
    def __init__(self, **kwargs):
        super(CustomCarousel, self).__init__(**kwargs)
        self.screens = []

    def on_index(self, *args):
        super(CustomCarousel, self).on_index(*args)
        current_tab = str(self.slides.index(self.current_slide))
        self.set_tab_states_to_normal()
        self.set_tab_down(current_tab)

    def set_tab_down(self, current_tab):
        try:
            tab = list(filter(lambda a: a.id == current_tab, self.parent.action_buttons))[0]
            tab.state = 'down'
        except IndexError:
            pass

    def set_tab_states_to_normal(self):
        for tab in self.parent.action_buttons:
            tab.state = 'normal'


class CustomActionBar(ActionBar):  # TODO Action previous action - getting back to prev screen
    def __init__(self, **kwargs):
        super(CustomActionBar, self).__init__(**kwargs)
        self.add_widget(ActionView())
        self.action_view.add_widget(ActionPrevious())


class CarouselWithActionBar(Screen):
    def __init__(self, **kwargs):
        super(CarouselWithActionBar, self).__init__(name='CarouselWithActionBar', **kwargs)
        self.actionBar = CustomActionBar(id='actionBar', background_image='jzielony.png',
                                         pos_hint={'x': 0, 'y': 0.9}, size_hint_y=0.1)
        self.carousel = CustomCarousel(id='carousel')
        self.add_widget(self.carousel)
        self.add_widget(self.actionBar)
        self.action_buttons = []

    def get_action_bar(self):
        return self.actionBar

    def get_carousel(self):
        return self.carousel

    def add_screen(self, screen):
        index = len(self.carousel.slides)
        screen.caro_index = index
        self.carousel.add_widget(screen)
        self.carousel.screens.append(screen)
        button_state = 'down' if index == 0 else 'normal'
        action_view = self.actionBar.action_view
        action_view.add_widget(ActionSeparator())
        action_button = ActionButton(id=str(index), size_hint=(None, 1), state=button_state,
                                     background_down='b5.png', color=(0, 0, 0, 1), text=screen.name,
                                     on_press=lambda a: self.carousel.load_slide(self.carousel.slides[int(a.id)]))
        self.action_buttons.append(action_button)
        action_view.add_widget(action_button)
