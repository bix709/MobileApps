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
        action_button = ActionButton(id=str(index), size_hint=(None, 1), state=button_state,
                                     background_down='b5.png', color=(0, 0, 0, 1), text=screen.name,
                                     on_press=lambda a: carousel.load_slide(carousel.slides[int(a.id)]))
        self.action_buttons.append(action_button)
        action_bar.add_widget(action_button)
