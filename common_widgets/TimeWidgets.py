# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from calendar import Calendar
from time import *

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from common_widgets.FittingLabels import FontFittingLabel, FontFittingButton

months_of_the_year = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec", 7: "Lipiec",
                      8: "Sierpień", 9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"}


class CommonCalendar(BoxLayout):
    def __init__(self, **kwargs):
        super(CommonCalendar, self).__init__(**kwargs)
        self.month_header_font_color = kwargs.get('month_header_font_color', (1, 1, 1, 1))
        self.days_header_font_color = kwargs.get('days_header_font_color', (1, 1, 1, 1))
        self.days_button_color = kwargs.get('days_button_color', (1, 1, 1, 1))
        self.orientation = "vertical"
        self.month_layout = GridLayout(cols=7)
        self.currently_displayed_month = (gmtime().tm_year, gmtime().tm_mon)
        self.display_month(*self.currently_displayed_month)

    def display_month(self, year, month):
        self.add_days_headers()
        displayed_month = Calendar().yeardatescalendar(year, 12)[0][month - 1]
        self.add_days_of_month(displayed_month, month)
        self.refresh_display()

    def add_days_of_month(self, displayed_month, month):
        for week_object in displayed_month:
            for day_object in week_object:
                intensivity = 1 if day_object.month == month else 0.75
                complete_date = (day_object.year, day_object.month, day_object.day)
                self.month_layout.add_widget(FontFittingButton(id='{}/{}/{}'.format(*complete_date),
                                                               text="{}".format(day_object.day),
                                                               color=self.days_button_color,
                                                               background_color=(1, 1, 1, intensivity),
                                                               on_release=lambda instance: self.on_choose(instance)))

    def add_days_headers(self):
        self.month_layout.clear_widgets()
        for x in ["Pon", "Wt", "Sr", "Czw", "Pt", "Sob", "Nd"]:
            self.month_layout.add_widget(Label(text=x, color=self.days_header_font_color))

    def next_month(self):
        year, month = self.currently_displayed_month
        self.currently_displayed_month = (year + 1, 1) if month == 12 else (year, month + 1)
        self.display_month(*self.currently_displayed_month)

    def previous_month(self):
        year, month = self.currently_displayed_month
        self.currently_displayed_month = (year - 1, 12) if month == 1 else (year, month - 1)
        self.display_month(*self.currently_displayed_month)

    def refresh_display(self):
        self.clear_widgets()
        self.add_widget(self.create_month_chooser())
        self.add_widget(self.month_layout)

    def create_month_chooser(self):
        month_chooser = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))
        displayed_year = self.currently_displayed_month
        month_chooser.add_widget(FontFittingButton(text="Poprzedni", on_release=lambda a: self.previous_month()))
        month_chooser.add_widget(
            FontFittingLabel(text="{} {}".format(months_of_the_year[displayed_year[1]], displayed_year[0]),
                             color=self.month_header_font_color))
        month_chooser.add_widget(FontFittingButton(text="Nastepny", on_release=lambda a: self.next_month()))
        return month_chooser

    def on_choose(self, instance):
        print(instance.id)


class Zegarek(Label):
    def __init__(self, **kwargs):
        super(Zegarek, self).__init__(**kwargs)
        self.pos = (200, 200)
        self.size = (500, 500)
        self.text = asctime()
        Clock.schedule_interval(self.refresh, 1)

    def refresh(self):
        self.text = asctime()
