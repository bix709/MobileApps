# -*- coding: utf-8 -*-
"""
    author: Tomasz Teter
    copyright : 5517 Company
"""
from calendar import monthrange


class EarningsCmdChooser(object):
    def __init__(self):
        self.get_earnings_cmd_from = {
            'week': self.get_weekly_earnings_cmd,
            'season': self.get_season_earnings_cmd,
            'month': self.get_monthly_earnings_cmd,
            'day': self.get_daily_earnings_cmd
        }

    def get_daily_earnings_cmd(self, period, user):
        date = "{}/{}/{}".format(period[1].year, period[1].month, period[1].day)
        cmd = "select sum(koszt) from lekcja where data = TO_DATE('{}', 'yyyy/mm/dd') ".format(date)
        if user:
            cmd += "and id_instruktora = {}".format(user.id)
        return cmd

    def get_monthly_earnings_cmd(self, period, user):
        month_length = monthrange(int(period[1].split("/")[0]), int(period[1].split("/")[1]))[1]
        cmd = "Select sum(koszt) from lekcja where data between TO_DATE('{month}/1', 'yyyy/mm/dd') " \
              "and TO_DATE('{month}/{month_length}', 'yyyy/mm/dd') ".format(month=period[1],
                                                                            month_length=month_length)
        if user:
            cmd += "and id_instruktora = {instructor}".format(instructor=user.id)
        return cmd

    def get_season_earnings_cmd(self, period, user):
        cmd = "Select sum(koszt) from lekcja where data between TO_DATE('{}/8/1', 'yyyy/mm/dd') " \
              "and TO_DATE('{}/6/1', 'yyyy/mm/dd') ".format(period[1].split("/")[0], period[1].split("/")[1])
        if user:
            cmd += "and id_instruktora = {}".format(user.id)
        return cmd

    def get_weekly_earnings_cmd(self, period, user):
        start_date = "{}/{}/{}".format(period[1].year, period[1].month, period[1].day)
        end_date = "{}/{}/{}".format(period[2].year, period[2].month, period[2].day)
        cmd = "Select sum(koszt) from lekcja where data between " \
              "TO_DATE('{}', 'yyyy/mm/dd') and TO_DATE('{}', 'yyyy/mm/dd') ".format(start_date, end_date)
        if user:
            cmd += "and id_instruktora = {}".format(user.id)
        return cmd
