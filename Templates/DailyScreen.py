# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Templates.Callbacks import GetDailyGraph
from common_widgets.FittingLabels import FontFittingButton
from common_widgets.FittingLabels import FontFittingLabel
from common_widgets.Screens import MyScreen
from time import gmtime


class DailyScreen(MyScreen):
    def __init__(self, *args, **kwargs):
        super(DailyScreen, self).__init__(size_hint_y=0.9, *args, **kwargs)
        today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.main_layout = BoxLayout(orientation='vertical')
        self.add_widget(self.main_layout)
        self.setup_widgets(today)

    def setup_widgets(self, day):  # TODO scrollable content
        today = "{}/{}/{}".format(gmtime().tm_year, gmtime().tm_mon, gmtime().tm_mday)
        self.main_layout.add_widget(FontFittingLabel(text='Grafik z dnia {}'.format(day)))
        self.main_layout.add_widget(FontFittingButton(text='Refresh', on_press=lambda a: self.refresh(day)))
        self.main_layout.add_widget(FontFittingButton(text='Pokaz dzisiejszy', on_press=lambda a: self.refresh(today)))
        self.get_day_schedule(day)

    def get_day_schedule(self, day):
        user = App.get_running_app().root.chosen_user
        db_args = args = ()
        db_kwargs = {'day': day, 'user': user}
        kwargs = {'instance': self}
        App.get_running_app().root.task_queue.put((GetDailyGraph(*db_args, **db_kwargs), args, kwargs))

    def refresh(self, day):
        self.main_layout.clear_widgets()
        self.setup_widgets(day)

    def add_hours(self, busy_hours):
        for hour in range(9, 21):
            try:
                lesson_info = busy_hours[hour]
                color = (1, 0, 0, 1)
            except KeyError:
                lesson_info = '{}.00 - {}.50'.format(hour, hour)
                color = (0, 1, 0, 1)
            finally:
                self.main_layout.add_widget(FontFittingButton(text='{}'.format(lesson_info),
                                                              on_press=lambda a: self.show_lesson_details(a),
                                                              background_color=color))

    def show_lesson_details(self, button_instance):
        print button_instance.text
