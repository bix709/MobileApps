# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os
from time import sleep

from plyer.platforms.android import activity

from adventureskiing.notification_service.notification_service import dispatch_incoming_notifications
from common_alarms.android_alarm import schedule_alarm_manager

if __name__ == '__main__':
    # dispatch_incoming_notifications(49)
    while True:
        print '5517Company'
        sleep(10)
