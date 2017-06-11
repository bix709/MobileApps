# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.instructions import InstructionGroup
from kivy.uix.actionbar import *
from kivy.uix.carousel import Carousel

from common_utilities.Utilities import ignored
from common_widgets.Screens import BackgroundAdjustableScreen, Rectangle


class CustomCarousel(Carousel):

    def __init__(self, **kwargs):
        super(CustomCarousel, self).__init__(**kwargs)
        self.background_instruction = InstructionGroup()
        self.bind(size=self.adjust_background)

    def setup_background(self):
        self.parent.canvas.before.add(self.background_instruction)

    def on_index(self, *args):
        super(CustomCarousel, self).on_index(*args)
        current_tab = str(self.slides.index(self.current_slide))
        self.set_tab_states_to_normal()
        self.set_tab_down(current_tab)
        self.adjust_background()
        App.get_running_app().root.commands_stack.append(self.current_slide)

    def set_tab_down(self, current_tab):
        try:
            tab = list(filter(lambda a: a.id == current_tab, self.parent.action_buttons))[0]
            tab.state = 'down'
        except IndexError:
            pass

    def set_tab_states_to_normal(self):
        for tab in self.parent.action_buttons:
            tab.state = 'normal'

    def adjust_background(self, *args, **kwargs):
        with ignored(Exception):
            self.background_instruction.clear()
            self.background_instruction.add(
                Rectangle(pos=self.pos, size=Window.size, source=self.parent.get_proper_background_image()))


class CustomActionBar(ActionBar):  # TODO Action previous action - getting back to prev screen
    def __init__(self, **kwargs):
        action_prev_properties = kwargs.pop('action_prev_properties')
        super(CustomActionBar, self).__init__(**kwargs)
        self.add_widget(ActionView(size_hint=(0.51, 1)))
        self.action_view.add_widget(ActionPrevious(**action_prev_properties))


class CarouselWithActionBar(BackgroundAdjustableScreen):
    def __init__(self, **kwargs):
        self.action_bar_properties = kwargs.pop('action_bar_properties', dict())
        self.action_button_properties = kwargs.pop('action_button_properties', dict())
        self.actionBar = self.action_buttons = self.carousel = None
        super(CarouselWithActionBar, self).__init__(name='CarouselWithActionBar', **kwargs)
        self.initialize()

    def initialize(self):
        self.actionBar = CustomActionBar(id='actionBar',
                                         **self.action_bar_properties)
        self.carousel = CustomCarousel(id='carousel', size_hint_y=0.9)
        self.add_widget(self.carousel)
        self.carousel.setup_background()
        self.add_widget(self.actionBar)
        self.action_buttons = []

    def add_screen(self, screen):
        index = len(self.carousel.slides)
        screen.caro_index = index
        self.carousel.add_widget(screen)
        button_state = 'down' if index == 0 else 'normal'
        action_view = self.actionBar.action_view
        # action_view.add_widget(ActionSeparator())  # TODO handle separators. ( throwing exception after resize )
        action_button = ActionButton(id=str(index), size_hint=(None, 1), state=button_state, text=screen.name,
                                     on_press=lambda a: self.carousel.load_slide(self.carousel.slides[int(a.id)]),
                                     **self.action_button_properties)
        self.action_buttons.append(action_button)
        action_view.add_widget(action_button)

    def reinitialize(self):
        self.clear_widgets()
        self.initialize()

    def get_proper_background_image(self):
        """ This method must return background that will be refreshed every carousel swip and resize. """
        return self.carousel._curr_slide().background_img

