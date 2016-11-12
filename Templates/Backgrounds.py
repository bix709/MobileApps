# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""

from threading import *
from concurrent.futures import *
from time import sleep
from Templates.DatabaseExecutor import SqlCommandsExecutor


class UpdatingWithDatabaseInBackground(Thread):
    def __init__(self, bag):
        """ Daemon thread ( program exits when only this thread is alive ) """
        super(UpdatingWithDatabaseInBackground, self).__init__()
        self.daemon = True
        self.bag = bag
        sql = SqlCommandsExecutor()
        self.tasks = [
            sql.fetch_logins
        ]

    def run(self):
        while True:
            self.update_bag_with_database_records()
            sleep(5)

    def update_bag_with_database_records(self):
        with ThreadPoolExecutor(max_workers=1) as executor:
            for task in self.tasks:
                future = executor.submit(task)
                if future.result():
                    self.bag.update(future.result())
                    print future.result()
