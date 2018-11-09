#!/usr/bin/env python3

"""xmascc.py: A small python extension for canteenie to print a countdown until christmas closing of FAU."""

import datetime
from datetime import date,timedelta


def get_countdown(fromdatetime,todatetime):
    """ get countdown until christmas closing of FAU """

    fromdate = date(fromdatetime.year, fromdatetime.month, fromdatetime.day)
    todate = date(todatetime.year, todatetime.month, todatetime.day)

    daygenerator = (fromdate + timedelta(x + 1) for x in range((todate - fromdate).days))

    countdown = sum(1 for day in daygenerator if day.weekday() < 5) + 1

    return "///// Nur noch %s Mal essen gehen bis zur Weihnachtsschließung der FAU. /////" %countdown
