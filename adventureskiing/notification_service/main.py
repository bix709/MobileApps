# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os
from time import sleep

from kivy.lib import osc

from adventureskiing.notification_service.notification_manager import NotificationManager


def stop_service(*args):
    notification_listener.stop()
    exit(0)

if __name__ == '__main__':
    session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
    notification_listener = NotificationManager(session_id)
    notification_listener.start()
    osc.init()
    oscid = osc.listen(ipAddr='0.0.0.0', port=3000)
    osc.bind(oscid, stop_service, '/stop')
    while True:  # Needs to be alive, because broadcast_receiver will no longer exist.
        osc.readQueue(oscid)
        sleep(10)
