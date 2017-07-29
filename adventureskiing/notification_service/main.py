# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os

from adventureskiing.notification_service.notification_service import dispatch_incoming_notifications

if __name__ == '__main__':
    session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
    dispatch_incoming_notifications(session_id)
