# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
import sys

from common_notifications.android_notification import notification_service

if __name__ == '__main__':
    notification_service(sys.argv[1])