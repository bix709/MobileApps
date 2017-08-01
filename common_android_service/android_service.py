# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from jnius import autoclass
from plyer.platforms.android import activity


class AndroidService(object):
    def __init__(self, service_name, arg):
        self.service = autoclass(activity.getPackageName() + '.Service' + service_name.capitalize())
        self.arg = arg

    def start(self):
        self.service.start(activity, str(self.arg))

    def stop(self):
        self.service.stop()
