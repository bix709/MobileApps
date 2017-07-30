# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os
from time import sleep
from adventureskiing.notification_service.notification_service import dispatch_incoming_notifications
from common_alarms.android_alarm import schedule_alarm_manager

if __name__ == '__main__':
    session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
    schedule_alarm_manager(20, lambda *args: dispatch_incoming_notifications(session_id))
    while True:
        sleep(10)
