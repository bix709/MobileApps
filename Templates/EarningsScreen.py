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

from Templates.Callbacks import GetEarnings
from common_callbacks.Callbacks import schedule_task
from common_widgets.FittingLabels import FontFittingButton, FontFittingLabel
from time import gmtime
from common_widgets.Screens import ScrollableScreen
from datetime import datetime, timedelta


class EarningsScreen(ScrollableScreen):  # TODO fix error obecny miesiac, test other dates, add UserChooser for admin.
    def __init__(self, **kwargs):
        self.today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.dates = self.get_dates()
        super(EarningsScreen, self).__init__(**kwargs)

    def get_dates(self):
        current_monday = (datetime.now() - timedelta(gmtime().tm_wday, 0))
        current_month = datetime.now().month
        current_year = gmtime().tm_year
        first_year = current_year if current_month > 7 else current_year - 1
        dates = {
            "Dzis": ("day", datetime.now()),
            "Wczoraj": ("day", (datetime.now() - timedelta(1, 0))),
            "Ten tydzien": ("week", current_monday, current_monday + timedelta(6, 0)),
            "Poprzedni Tydzien": ("week", current_monday - timedelta(7, 0), current_monday - timedelta(1, 0)),
            "Obecny miesiac": ("month", current_month),
            "Poprzedni miesiac": ("month", current_month - 1 if current_month != 1 else 12),
            "Obecny sezon": ("season", "{}/{}".format(first_year, first_year + 1)),
            "Poprzedni sezon": ("season", "{}/{}".format(first_year - 1, first_year))
        }
        return dates

    def setup_widgets(self):
        self.setup_period_chooser()

    def setup_period_chooser(self):
        period_chooser = DropDown()
        for x in self.dates.keys():
            period_chooser.add_widget(Button(text="{}".format(x), size_hint_y=None, height=33,
                                             on_release=lambda a: period_chooser.select(a.text)))
        self.choosen = FontFittingButton(text="Dzis", size_hint=(1, 1))
        self.choosen.bind(on_release=period_chooser.open)
        period_chooser.bind(on_select=lambda instance, z: setattr(self.choosen, 'text', z))
        self.main_layout.add_widget(FontFittingLabel(text="Wybierz okres rozliczeniowy:", size_hint=(1, 1)))
        self.main_layout.add_widget(self.choosen)
        self.main_layout.add_widget(FontFittingButton(text="Wybierz inny dzień", size_hint=(1, 1),
                                                      on_press=lambda a: self.choose_other_date()))
        self.main_layout.add_widget(FontFittingButton(text="Wyswietl", size_hint=(1, 1),
                                                      on_press=lambda a: self.display_choosen()))

    def choose_other_date(self):
        OtherDatePopup(caller=self).open()

    def display_choosen(self, period=None):
        if period is None:
            period = self.dates[self.choosen.text]
        db_kwargs = {
            'period': period,
            'user': App.get_running_app().root.choosen_user
        }
        schedule_task(callback=GetEarnings(**db_kwargs), cb_args=tuple(), cb_kwargs={'instance': self})

    def show_earnings(self, total_earns):
        self.main_layout.clear_widgets()
        self.setup_widgets()
        if total_earns is not None:
            self.main_layout.add_widget(FontFittingLabel(text="Zarobione łącznie: {}".format(total_earns)))
            self.main_layout.add_widget(FontFittingLabel(text="Na czysto: {}".format(total_earns / 2)))


class OtherDatePopup(Popup):
    def __init__(self, caller, **kwargs):
        super(OtherDatePopup, self).__init__(title="Podaj date (rok/miesiac/dzien)", auto_dismiss=True,
                                             size_hint=(0.5, 0.4), **kwargs)
        self.caller = caller
        main_layout = BoxLayout(orientation='vertical')
        self.input = TextInput(focus=False, multiline=False, size_hint=(1, 1),
                               on_text_validate=lambda a: self.display_choosen())
        self.input.focus = True
        main_layout.add_widget(self.input)
        main_layout.add_widget(FontFittingButton(text="Wyswietl", size_hint=(1, 1),
                                                 on_press=lambda a: self.display_choosen()))
        self.add_widget(main_layout)

    def display_choosen(self):
        try:
            date = [int(each) for each in self.input.text.split("/")]
            self.caller.display_choosen(("day", datetime(*date)))
            self.dismiss()
        except:
            self.dismiss()
