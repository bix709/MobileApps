# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from kivy.lib import osc
from kivy.utils import platform


def start_notification_service(session_id):
    if platform == 'android':
        from jnius import autoclass
        from plyer.platforms.android import activity
        service = autoclass(activity.getPackageName() + '.Service' + 'Notify')
        mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
        service.start(mActivity, str(session_id))
        return service


def stop_notification_service():
    osc.init()
    osc.sendMsg('/stop', [], port=3000)
