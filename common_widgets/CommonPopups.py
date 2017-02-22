# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from Templates.Callbacks import PasswordChange
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import FontFittingButton, FontFittingLabel


class CommonPopup(Popup):
    def __init__(self, **kwargs):
        super(CommonPopup, self).__init__(size_hint_x=0.8, size_hint_y=0.9, auto_dismiss=True, **kwargs)
        self.main_layout = BoxLayout(orientation='vertical')
        self.add_widget(self.main_layout)
        self.setup_widgets()

    def setup_widgets(self):
        esc_layout = BoxLayout(size_hint_x=0.2, pos_hint={"x": 0.8})
        esc_layout.add_widget(FontFittingButton(text="Esc", on_press=lambda a: self.dismiss()))
        self.main_layout.add_widget(esc_layout)


class PasswordChanger(CommonPopup):
    def __init__(self, **kwargs):
        super(PasswordChanger, self).__init__(title="Zmien haslo", **kwargs)

    def setup_widgets(self):
        super(PasswordChanger, self).setup_widgets()
        self.setup_input_fields()
        self.main_layout.add_widget(FontFittingButton(text="Zatwierdz", on_press=lambda a: self.confirm()))

    def setup_input_fields(self):
        self.main_layout.add_widget(FontFittingLabel(text="Stare haslo:"))
        self.main_layout.add_widget(TextInput(id='old', focus=False, password=True, multiline=False,
                                              on_text_validate=lambda a: self.focus_input('new')))
        self.focus_input('old')
        self.main_layout.add_widget(FontFittingLabel(text="Nowe haslo:"))
        self.main_layout.add_widget(TextInput(id='new', focus=False, password=True, multiline=False,
                                              on_text_validate=lambda a: self.focus_input('repeated')))
        self.main_layout.add_widget(FontFittingLabel(text="Powtorz Nowe haslo:"))
        self.main_layout.add_widget(TextInput(id='repeated', focus=False, password=True, multiline=False,
                                              on_text_validate=lambda a: self.confirm()))

    def focus_input(self, input_id):
        self.get_input(input_id).focus = True

    def get_input(self, input_id):
        return list(filter(lambda a: a.id == input_id, self.main_layout.children))[0]

    def confirm(self):
        if not self.get_input('new').text == self.get_input('repeated').text:
            self.on_wrong_attempt()
        else:
            schedule_task(PasswordChange(old_pw=hash(self.get_input('old').text),
                                         new_pw=hash(self.get_input('new').text),
                                         user=App.get_running_app().root.choosen_user), tuple(), {'instance': self})

    def on_successful_change(self):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(FontFittingLabel(text="[color=00FF00]Hasło zostało zmienione poprawnie.[/color]",
                                                     markup=True))
        self.bind(on_dismiss=self.dismiss_after_success)
        self.main_layout.add_widget(FontFittingButton(text="Ok", on_release=lambda a: self.dismiss()))

    def on_wrong_attempt(self):
        for input_id in ['old', 'new', 'repeated']:
            self.get_input(input_id).text = ''
        self.focus_input('old')
        self.main_layout.add_widget(FontFittingLabel(text="[b][color=FF0000]Nie poprawne dane![/color][/b]",
                                                     markup=True))

    def dismiss_after_success(self, *args, **kwargs):
        super(PasswordChanger, self).on_dismiss()
        App.get_running_app().root.logout()
