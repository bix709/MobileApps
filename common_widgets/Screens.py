# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from common_widgets.FittingLabels import FontFittingLabel, FontFittingButton


class BackgroundAdjustableScreen(Screen):
    def __init__(self, size=Window.size, **kwargs):
        self.background_img = kwargs.pop('background_image', None)
        super(BackgroundAdjustableScreen, self).__init__(size=size, **kwargs)
        self.background_instruction = InstructionGroup()
        self.set_up_background_image()
        self.bind(size=self.fit_to_window)

    def set_up_background_image(self):
        if self.background_img:
            self.background_instruction.add(Rectangle(pos=self.pos, size=Window.size, source=self.background_img))
            self.canvas.add(self.background_instruction)

    def fit_to_window(self, *args):
        rectangle = (Rectangle(pos=self.pos, size=Window.size, source=self.background_img))
        self.background_instruction.clear()
        self.background_instruction.add(rectangle)


class LoginScreen(BackgroundAdjustableScreen):
    def __init__(self, loginbutton_properties, credential_label_properties, **kwargs):
        super(LoginScreen, self).__init__(name='Login Screen', **kwargs)
        self.loginbutton_properties = loginbutton_properties
        self.credential_label_properties = credential_label_properties
        self.font_color = kwargs.get('font_color', (0, 0, 0, 1))
        self.__username_input = self.__password_input = None
        self.main_layout = BoxLayout(id='MainLayout', orientation='vertical', size_hint_x=0.8,
                                     size_hint_y=0.8, pos_hint={"x": 0.1, "y": 0.15})
        self.add_widget(self.main_layout)
        self.initialize()

    def initialize(self):
        self.create_main_layout()
        self.__username_input.focus = True

    def create_main_layout(self, wrong_login=False):
        if wrong_login:
            self.main_layout.add_widget(
                FontFittingLabel(markup=True, color=(1, 1, 1, 1), font_size=18, size_hint_y=0.20,
                                 text="[b][color=FF0000]Zły login lub hasło![/color][/b]"))
        self.__username_input = TextInput(multiline=False, id='Username', focus=False, size_hint_y=0.20,
                                          on_text_validate=lambda a: self.focus_password())
        self.__password_input = TextInput(multiline=False, id='Password', focus=False, size_hint_y=0.20,
                                          password=True,
                                          on_text_validate=lambda a: self.parent.handle_login(
                                              self.__username_input.text,
                                              str(hash(a.text))))
        self.main_layout.add_widget(FontFittingLabel(text="Login:", **self.credential_label_properties))
        self.main_layout.add_widget(self.__username_input)
        self.main_layout.add_widget(FontFittingLabel(text="Hasło:", **self.credential_label_properties))
        self.main_layout.add_widget(self.__password_input)
        self.main_layout.add_widget(
            FontFittingButton(on_press=lambda a: self.parent.handle_login(
                                                          self.__username_input.text,
                                                          self.__password),
                              **self.loginbutton_properties))
        self.__password_input.text = self.__username_input.text = ''

    @property
    def __password(self):
        return str(hash(self.__password_input.text))

    def focus_password(self):
        self.__password_input.focus = True

    def wrong_login_attempt(self):
        self.main_layout.clear_widgets()
        self.create_main_layout(wrong_login=True)
        self.__username_input.focus = True

    def reinitialize(self):
        self.main_layout.clear_widgets()
        self.initialize()


class ScrollableScreen(BackgroundAdjustableScreen):
    def __init__(self, *args, **kwargs):
        super(ScrollableScreen, self).__init__(*args, **kwargs)
        self.main_layout = GridLayout(cols=1, size_hint_y=None, height=Window.height)
        self.main_layout.bind(minimum_height=self.main_layout.setter('height'))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.main_layout)
        self.add_widget(scroll)
        self.setup_widgets()
        self.main_layout.height = Window.height * 0.9

    def setup_widgets(self):
        pass
