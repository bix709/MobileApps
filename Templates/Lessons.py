# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from Templates.Callbacks import InsertNewLesson, RemoveLesson
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import FontFittingButton, FontFittingLabel


class LessonPopup(Popup):
    def __init__(self, date, lesson_info, from_today_screen=False, **kwargs):
        super(LessonPopup, self).__init__(title="Dzien {}, Godzina {}".format(date, lesson_info['hour']),
                                          size_hint_x=0.75, size_hint_y=0.9, auto_dismiss=True, **kwargs)
        self.main_layout = BoxLayout(orientation='vertical')
        self.date = date
        self.from_today_screen = from_today_screen
        self.hour = lesson_info['hour']
        self.lesson_info = lesson_info
        self.setup_widgets()
        self.add_widget(self.main_layout)

    def setup_widgets(self):
        esc_layout = BoxLayout(size_hint_x=0.2, pos_hint={"x": 0.8})
        esc_layout.add_widget(FontFittingButton(text="Esc", on_press=lambda a: self.dismiss()))
        self.main_layout.add_widget(esc_layout)
        self.setup_input_fields()
        self.setup_number_chooser()
        self.main_layout.add_widget(FontFittingButton(text="Zatwierdz", on_press=lambda a: self.confirm()))
        self.main_layout.add_widget(FontFittingButton(text="Anuluj", on_press=lambda a: self.cancel_lesson()))

    def setup_input_fields(self):
        self.main_layout.add_widget(FontFittingLabel(text="Imie:"))
        imie = self.lesson_info['imie'] if 'imie' in self.lesson_info.keys() else ""
        wiek = self.lesson_info['wiek'] if 'wiek' in self.lesson_info.keys() else ""
        self.name_input = TextInput(multiline=False, focus=False, id='imie', text="{}".format(imie),
                                    on_text_validate=lambda a: self.focus_age())
        self.name_input.focus = True
        self.main_layout.add_widget(self.name_input)
        self.main_layout.add_widget(FontFittingLabel(text="Wiek:"))
        self.age_input = TextInput(multiline=False, id='wiek', text="{}".format(wiek), focus=False)
        self.main_layout.add_widget(self.age_input)

    def focus_age(self):
        self.age_input.focus = True

    def setup_number_chooser(self):
        number_chooser = DropDown()
        for x in range(6):
            number_chooser.add_widget(Button(text="%s" % x, size_hint_y=None, height=33,
                                             on_release=lambda a: number_chooser.select(a.text)))
        ilosc_osob = self.lesson_info['ilosc_osob'] if 'ilosc_osob' in self.lesson_info.keys() else "0"
        self.choosen = FontFittingButton(text="{}".format(ilosc_osob), size_hint=(1, 1))
        self.choosen.bind(on_release=number_chooser.open)
        number_chooser.bind(on_select=lambda instance, z: setattr(self.choosen, 'text', z))
        self.main_layout.add_widget(FontFittingLabel(text="Ilosc osob:", size_hint=(1, 1)))
        self.main_layout.add_widget(self.choosen)

    def confirm(self):
        lesson_id = self.lesson_info['lesson_id'] if 'lesson_id' in self.lesson_info.keys() else "0"
        db_kwargs = {
            'name': self.name_input.text,
            'age': self.age_input.text,
            'number_of_people': self.choosen.text,
            'date': self.date,
            'user': App.get_running_app().root.choosen_user,
            'hour': self.hour,
            'lesson_id': lesson_id
        }
        schedule_task(callback=InsertNewLesson(**db_kwargs), cb_args=(), cb_kwargs={'instance': self})

    def on_successful_execution(self, *args, **kwargs):
        if App.get_running_app().root.logged_user.privileges != "Admin":
            App.get_running_app().root.choosen_user = App.get_running_app().root.logged_user
        caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
        daily_graph = list(filter(lambda a: a.name == "DailyScreen", caro.screens))[0]
        daily_graph.refresh(self.date)
        self.dismiss()

    def cancel_lesson(self):
        lesson_id = self.lesson_info['lesson_id'] if 'lesson_id' in self.lesson_info.keys() else "0"
        db_kwargs = {
            'lesson_id': lesson_id
        }
        schedule_task(callback=RemoveLesson(**db_kwargs), cb_args=(), cb_kwargs={'instance': self})
