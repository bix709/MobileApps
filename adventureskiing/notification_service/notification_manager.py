import os
from os.path import dirname, realpath
from kivy.utils import platform
from adventureskiing.Database.MySQL.db_commands import SqlCommands

if platform == 'android':
    from common_alarms.android_alarm import AlarmManager
    from plyer.platforms.android import activity
    from common_notifications.android_notification import AndroidNotification as notifier
    notification_event = '{}.NOTIFICATION_ALARM'.format(activity.getPackageName())


class NotificationManager(object):
    def __init__(self, session_id):
        super(NotificationManager, self).__init__()
        self.session_id = session_id
        self.alarm_manager = AlarmManager(notification_event)
        self.notifier = notifier()

    def dispatch_incoming_notifications(self, *args):
        notifications = SqlCommands.get_notifications(self.session_id)
        for data, godzina, ilosc_os, operacja in notifications:
            message, ticker = self.get_message_ticker(data, godzina, ilosc_os, operacja)
            icon_path = os.path.join(dirname(dirname(realpath(__file__))), 'adventureskiing', 'graphics', 'logo.png')
            self.notifier.notify(title=ticker, message=message, app_name='ASy',
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
