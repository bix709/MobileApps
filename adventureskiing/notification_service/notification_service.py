# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os
from time import sleep
from kivy.utils import platform
from os.path import dirname, realpath
from adventureskiing.Database.MySQL.db_commands import SqlCommands


def start_notification_service(session_id):
    if platform == 'android':
        from jnius import autoclass
        from plyer.platforms.android import activity
        service = autoclass(activity.getPackageName() + '.Service' + 'Notify')
        mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        service.start(mActivity, str(session_id))
        return service


def dispatch_incoming_notifications(session_id):
    if platform == 'android':
        from common_notifications.android_notification import AndroidNotification
        notification = AndroidNotification()
        while True:
            notifications = SqlCommands.get_notifications(session_id)
            for data, godzina, ilosc_os, operacja in notifications:
                message, ticker = get_message_ticker(data, godzina, ilosc_os, operacja)
                icon_path = os.path.join(dirname(dirname(realpath(__file__))), 'adventureskiing', 'graphics', 'logo.png')
                notification.notify(title=ticker, message=message, app_name='ASy',
                                    app_icon=icon_path, ticker=ticker)


def get_message_ticker(data, godzina, ilosc_os, operacja):
    if operacja == "ADD":
        message = '{data}, o godzinie {godzina}({ilosc_os}os.)'.format(ilosc_os=ilosc_os,
                                                                       data=data,
                                                                       godzina=godzina)
        ticker = 'Nowa lekcja'
    else:
        message = '{data}, o godzinie {godzina}({ilosc_os}os.)'.format(ilosc_os=ilosc_os,
                                                                       data=data,
                                                                       godzina=godzina)
        ticker = 'Lekcja odwolana'
    return message, ticker
