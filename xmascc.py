#!/usr/bin/env python3

"""xmascc.py: A small python extension for canteenie to print a countdown until christmas closing of FAU."""

import configparser
import datetime
import os
from datetime import date,timedelta

script_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(script_path + '/canteenie.ini')

now = datetime.datetime.now()
last_workday = datetime.datetime.strptime(config.get('xmascc', 'last_workday'), '%Y-%m-%d')

fromdate = date(now.year, now.month, now.day)
todate = date(last_workday.year, last_workday.month, last_workday.day)

daygenerator = (fromdate + timedelta(x + 1) for x in range((todate - fromdate).days))

countdown = sum(1 for day in daygenerator if day.weekday() < 5) + 1

def get_countdown():
  return "///// Nur noch %s Mal essen gehen bis zur Weihnachtsschließung der FAU. /////" %countdown
