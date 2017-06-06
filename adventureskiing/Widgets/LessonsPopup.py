# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput

from adventureskiing.Database.Callbacks import InsertNewLesson, RemoveLesson
from common_widgets.CommonPopups import CommonPopup
from common_widgets.FittingLabels import FontFittingButton, FontFittingLabel
from adventureskiing.Widgets.DailyScreen import *


class LessonPopup(CommonPopup):  # TODO refactoring ( focusing inputs etc. )
    def __init__(self, date, lesson_info, from_today_screen=False, **kwargs):
        self.date = date
        self.from_today_screen = from_today_screen
        self.hour = lesson_info['hour']
        self.lesson_info = lesson_info
        super(LessonPopup, self).__init__(title="Dzien {}, Godzina {}".format(date, lesson_info['hour']), **kwargs)
        self.bind(on_dismiss=lambda a: self.correct_choosen_user())

    def correct_choosen_user(self):
        if App.get_running_app().root.logged_user.privileges != "Admin":
            App.get_running_app().root.choosen_user = App.get_running_app().root.logged_user

    def setup_widgets(self):
        super(LessonPopup, self).setup_widgets()
        self.setup_input_fields()
        self.setup_number_chooser()
        self.main_layout.add_widget(FontFittingButton(text="Zatwierdz", on_press=lambda a: self.confirm()))
        self.main_layout.add_widget(FontFittingButton(text="Usuń lekcję", on_press=lambda a: self.cancel_lesson()))

    def setup_input_fields(self):
        self.main_layout.add_widget(FontFittingLabel(text="Imie:"))
        imie = self.lesson_info.get('imie', "")
        wiek = self.lesson_info.get('wiek', "")
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
            number_chooser.add_widget(FontFittingButton(text="%s" % x, size_hint_y=None, height=number_chooser.height,
                                                        on_release=lambda a: number_chooser.select(a.text)))
        ilosc_osob = self.lesson_info.get('ilosc_osob', "0")
        self.choosen = FontFittingButton(text="{}".format(ilosc_osob), size_hint=(1, 1))
        self.choosen.bind(on_release=lambda a: number_chooser.open(self.choosen))
        number_chooser.bind(on_select=lambda instance, z: setattr(self.choosen, 'text', z))
        self.main_layout.add_widget(FontFittingLabel(text="Ilosc osob:", size_hint=(1, 1)))
        self.main_layout.add_widget(self.choosen)

    def confirm(self):
        lesson_id = self.lesson_info.get('lesson_id', '0')
        db_kwargs = {
            'name': self.name_input.text,
            'age': self.age_input.text,
            'number_of_people': self.choosen.text,
            'date': self.date,
            'user': App.get_running_app().root.choosen_user,
            'hour': self.hour,
            'lesson_id': lesson_id
        }
        schedule_task(callback=InsertNewLesson(**db_kwargs), instance=self)

    def on_successful_execution(self, added_successfully, **kwargs):
        if added_successfully:
            caro = App.get_running_app().root.get_screen("CarouselWithActionBar").carousel
            daily_graph = list(filter(lambda a: a.id == 'DailyScreen', caro.slides))[0]
            daily_graph.refresh(self.date)
            self.dismiss()
        elif added_successfully is False:
            self.display_error('Lekcja juz istnieje! Odśwież swój grafik!')
        else:
            self.display_error('Wypełnij pola poprawnymi danymi!')

    def display_error(self, error_msg):
        self.main_layout.clear_widgets()
        self.setup_widgets()
        self.main_layout.add_widget(
            FontFittingLabel(text="[b][color=FF0000]{msg}[/color][/b]".format(msg=error_msg),
                             markup=True))

    def cancel_lesson(self):
        lesson_id = self.lesson_info.get('lesson_id', "0")
        db_kwargs = {
            'lesson_id': lesson_id
        }
        schedule_task(callback=RemoveLesson(**db_kwargs), instance=self)
