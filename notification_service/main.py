# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os

import plyer
from os.path import dirname, realpath

from common_utilities.Utilities import ignored
from notification_service.android_notification import notification_service

if __name__ == '__main__':
    with ignored(Exception):
        session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
        plyer.notification.notify(title=session_id, message=session_id, app_name='ASy',
                                  app_icon=os.path.join(dirname(dirname(realpath(__file__))),
                                                        'adventureskiing', 'graphics', 'logo.png'),
                                  ticker=session_id)
    notification_service(session_id)
