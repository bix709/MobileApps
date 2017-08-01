# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.lib import osc
from kivy.utils import platform


def start_notification_service(session_id):
    if platform == 'android':
        from common_android_service.android_service import AndroidService
        AndroidService(service_name='Notify', arg=session_id).start()


def stop_notification_service():
    if platform == 'android':
        osc.init()
        osc.sendMsg('/stop', [], port=3000)