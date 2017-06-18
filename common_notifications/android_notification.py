# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from time import sleep

import plyer
from kivy.app import App
from kivy.utils import platform
from adventureskiing.Database.MySQL.db_commands import SqlCommands


def setup_notifications_checks(session_id):
    if platform == 'android':
        import android
        android.start_service('Notification Name', 'Notification Message', session_id)


def notification_service(session_id):
    while True:
        notifications = SqlCommands.get_notifications(session_id)
        for data, godzina, ilosc_os, operacja in notifications:
            title = "Adventure Skiing"
            message, ticker = get_message_ticker(data, godzina, ilosc_os, operacja)
            plyer.notification.notify(title=title, message=message, app_name='ASy',
                                      app_icon='adventureskiing/graphics/logo.png', ticker=ticker)
        sleep(10)


def get_message_ticker(data, godzina, ilosc_os, operacja):
    if operacja == "ADD":
        message = 'Nowa lekcja({ilosc_os}os.) dnia: {data}, o godzinie {godzina}'.format(ilosc_os=ilosc_os,
                                                                                         data=data,
                                                                                         godzina=godzina)
        ticker = 'Nowa lekcja'
    else:
        message = 'Anulowano lekcje({ilosc_os}os.) dnia: {data}, o godzinie {godzina}'.format(ilosc_os=ilosc_os,
                                                                                              data=data,
                                                                                              godzina=godzina)
        ticker = 'Lekcja odwolana'
    return message, ticker
