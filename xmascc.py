#!/usr/bin/env python3

"""xmascc.py: A small python extension for canteenie to print a countdown until christmas closing of FAU."""

import datetime
from datetime import date,timedelta

#fromdate = date(2017,11,7)
now = datetime.datetime.now()

fromdate = date(now.year, now.month, now.day)
todate = date(2017,12,22)

daygenerator = (fromdate + timedelta(x + 1) for x in range((todate - fromdate).days))

countdown = sum(1 for day in daygenerator if day.weekday() < 5) + 1

def get_countdown():
  return "///// Nur noch %s Mal essen gehen bis zur Weihnachtsschließung der FAU. /////" %countdown
