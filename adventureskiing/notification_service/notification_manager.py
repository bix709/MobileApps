import os
from os.path import dirname, realpath
from kivy.utils import platform
from plyer.platforms.android import activity
from adventureskiing.Database.MySQL.db_commands import SqlCommands
from common_alarms.android_alarm import AlarmManager


class NotificationManager(object):
    def __init__(self, session_id):
        super(NotificationManager, self).__init__()
        self.alarm_manager = AlarmManager('{}.NOTIFICATION_ALARM'.format(activity.getPackageName()))
        self.session_id = session_id

    def dispatch_incoming_notifications(self, *args):
        if platform == 'android':
            from common_notifications.android_notification import AndroidNotification
            notifier = AndroidNotification()
            notifications = SqlCommands.get_notifications(self.session_id)
            for data, godzina, ilosc_os, operacja in notifications:
                message, ticker = self.get_message_ticker(data, godzina, ilosc_os, operacja)
                icon_path = os.path.join(dirname(dirname(realpath(__file__))), 'adventureskiing', 'graphics', 'logo.png')
                notifier.notify(title=ticker, message=message, app_name='ASy',
                                app_icon=icon_path, ticker=ticker)

    def get_message_ticker(self, data, godzina, ilosc_os, operacja):
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

    def start(self):
        self.alarm_manager.schedule_interval(20, self.dispatch_incoming_notifications)

    def stop(self):
        self.alarm_manager.stop_alarm()
