# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os

from adventureskiing.notification_service import dispatch_incoming_notifications
from common_utilities.Utilities import ignored

if __name__ == '__main__':
    with ignored(Exception):
        session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
        dispatch_incoming_notifications(session_id)
