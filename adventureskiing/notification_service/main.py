# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import os

if __name__ == '__main__':
    session_id = int(os.getenv('PYTHON_SERVICE_ARGUMENT'))
    # AlarmManager().schedule(interval=20, callback=lambda *args: dispatch_incoming_notifications(session_id))