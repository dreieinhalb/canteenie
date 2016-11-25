#!/usr/bin/env python3

"""xmascc.py: A small python extension for canteenie to print a countdown until christmas closing of FAU."""

import datetime
from datetime import date,timedelta

#fromdate = date(2016,12,23)
now = datetime.datetime.now()

fromdate = date(now.year, now.month, now.day)
todate = date(2016,12,23)

daygenerator = (fromdate + timedelta(x + 1) for x in range((todate - fromdate).days))

countdown = sum(1 for day in daygenerator if day.weekday() < 5) + 1

def print_countdown():
  print("///// Nur noch %s Mal essen gehen bis zur Weihnachtsschließung der FAU. /////" %countdown)
