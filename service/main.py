# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os

import plyer

from common_notifications.android_notification import notification_service
from common_utilities.Utilities import ignored

if __name__ == '__main__':
    plyer.vibrator.vibrate(10000)
    with ignored(Exception):
        session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
    notification_service(session_id)