# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from common_widgets.FittingLabels import FontFittingLabel


class MyScreen(Screen):
    def __init__(self, background_img=None, size=Window.size, **kwargs):
        super(MyScreen, self).__init__(size=size, **kwargs)
        self.background_img = background_img
        self.background_instruction = InstructionGroup()
        self.set_up_background_image()
        Window.bind(on_resize=self.fit_to_window)

    def set_up_background_image(self):
        if self.background_img:
            self.background_instruction.add(Rectangle(pos=self.pos, size=self.size, source=self.background_img))
            self.canvas.add(self.background_instruction)

    def fit_to_window(self, window, width, height):
        rectangle = (Rectangle(pos=self.pos, size=(width, height), source=self.background_img))
        background = self.get_background_instruction()
        background.clear()
        background.add(rectangle)

    def get_background_instruction(self):
        return list(filter(lambda a: a == self.background_instruction, self.canvas.children))[0]


class LoginScreen(MyScreen):
    def __init__(self, background_img=None, **kwargs):
        super(LoginScreen, self).__init__(background_img=background_img, **kwargs)
        self.name = 'Login Screen'
        self.add_widget(self.create_main_layout())
        self.get_username_input().focus = True

    def create_main_layout(self, wrong_login=False):
        main_layout = BoxLayout(id='MainLayout', orientation='vertical', size_hint_x=0.8,
                                size_hint_y=0.8, pos_hint={"x": 0.1, "y": 0.15})
        if wrong_login:
            main_layout.add_widget(FontFittingLabel(markup=True, color=(1, 1, 1, 1), font_size=18, size_hint_y=0.20,
                                                    text="[b][color=FF0000]Wrong username or password ![/color][/b]"))
        main_layout.add_widget(Label(color=(1, 1, 1, 1), size_hint_y=0.30, font_size=30, text="Username:"))
        main_layout.add_widget(TextInput(multiline=False, id='Username', focus=False, size_hint_y=0.20,
                                         on_text_validate=lambda a: self.focus_password()))
        main_layout.add_widget(Label(color=(1, 1, 1, 1), size_hint_y=0.30, font_size=30, text="Password:"))
        main_layout.add_widget(TextInput(multiline=False, id='Password', focus=False, size_hint_y=0.20,
                                         password=True, on_text_validate=
                                         lambda a: self.parent.handle_login(self.get_username(), str(hash(a.text)))))
        main_layout.add_widget(Button(background_normal="b3.png", text="Zaloguj!", color=(1, 1, 1, 1),
                                      size_hint_y=0.30, font_size=30, on_press=lambda a:
            self.parent.handle_login(self.get_username(), self.get_password())))
        return main_layout

    def get_main_layout(self):
        return list(filter(lambda a: a.id == 'MainLayout', self.children))[0]

    def get_username_input(self):
        return list(filter(lambda a: a.id == 'Username', self.get_main_layout().children))[0]

    def get_password_input(self):
        return list(filter(lambda a: a.id == 'Password', self.get_main_layout().children))[0]

    def get_username(self):
        return self.get_username_input().text

    def get_password(self):
        return str(hash(self.get_password_input().text))

    def focus_password(self):
        self.get_password_input().focus = True

    def wrong_login_attempt(self):
        self.clear_widgets()
        self.add_widget(self.create_main_layout(wrong_login=True))
        self.get_username_input().focus = True
