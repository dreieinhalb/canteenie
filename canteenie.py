#!/usr/bin/env python3

"""canteenie.py: A small python script that prints today's canteen/mensa on console using openmensa API."""

import argparse
import configparser
import datetime
import os
import re
import xmascc
from openmensa import OpenMensa as openmensa
from termcolor import colored


# read config file
script_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(script_path + '/canteenie.ini')


# map for assignment of IDs for FAU canteens
fau_mensa = {
    "lmpl" : 264,
    "sued" : 256,
    "isch" : 265,
}

# map for assignment of categories to abbreviations
category_map = {
    "Vegetarisch" : "V",
    "Schwein"     : "S",
    "Rind"        : "R",
    "Geflügel"    : "G",
    "Fisch"       : "F",
}


def valid_date(s):
    """ validate passed date and throw exception if it is not valid """
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def colorize(text, color):
    """ return colored text
        (only if lite option is not set)
    """
    if not args['lite']:
        return colored(text, color)
    else:
        return text

def intent():
    """ return intentation
        (only if lite option is not set)
    """
    if not args['lite']:
        return "\t"
    else:
        return ''


# command line arguments
parser = argparse.ArgumentParser(description='A small python script that prints today\'s canteen/mensa menu for FAU on console.')
parser.add_argument(
    '-m', '--mensa',
    help     = 'for which mensa? (lmpl: Erlangen Langemarckplatz (default), sued: Erlangen Süd, isch: Nürnberg Insel Schütt)',
    default  = "lmpl",
    choices  = ['lmpl', 'sued', 'isch'],
    required = False,
)
parser.add_argument(
    '-i', '--id',
    help     = 'for which ID on openmensa.org?',
    default  = argparse.SUPPRESS, # don't define key if not given
    required = False,
)
parser.add_argument(
    '-d', '--date',
    help     = 'for which date (YYYY-MM-DD)?',
    default  = argparse.SUPPRESS, # don't define key if not given
    type     = valid_date,
    required = False,
)
parser.add_argument(
    '-l', '--lite',
    help     = 'disable ascii art header and color (lite view)',
    action   = 'store_true',
    default  = False,
    required = False,
)
parser.add_argument(
    '-p', '--price',
    help     = 'prices for which group? (employees (default), students, others)',
    default  = "employees",
    choices  = ['employees', 'students', 'others'],
    required = False,
)
parser.add_argument(
    '--no-xmascc',
    help     = 'disable christmas closing countdown',
    action   = 'store_true',
    default  = False,
    required = False,
)
args = vars(parser.parse_args())


# argument computing
# use mensa Langemarckplatz as default, or use given ID from args
openmensa_id = 264
date         = datetime.datetime.now()
if 'mensa' in args:
    openmensa_id = fau_mensa[args['mensa']]
if 'id'    in args:
    openmensa_id = args['id']
# use today as default or given date from args
if 'date'  in args: date = args['date']


# get meals from openmensa API
try:
    meals = openmensa.get_meals_by_day(openmensa_id, date.strftime("%Y-%m-%d"))
except Exception as e:
    print("Found no meal for given date at OpenMensaAPI, maybe you are looking for a too old, too far away or closed day.")
    raise SystemExit


# print header (ascii art only in non lite version)
if not args['lite']:
    iten = intent()
    print(iten + colorize("                             ",'yellow'))
    print(iten + colorize(" __  __                      ",'yellow'))
    print(iten + colorize("|  \/  | ___ _ __  ___  __ _ ",'yellow'))
    print(iten + colorize("| |\/| |/ _ \ '_ \/ __|/ _` |",'yellow'))
    print(iten + colorize("| |  | |  __/ | | \__ \ (_| |",'yellow'))
    print(iten + colorize("|_|  |_|\___|_| |_|___/\__,_|",'yellow'))
    print(iten + colorize("                             ",'yellow'))
print(intent() + colorize("//////// " + date.strftime("%d.%m.%Y") + " /////////", 'green'))
print("")


# generate/print menu
# set counter for numbering meals
i = 1;
for meal in meals:
    number = "(" + str(i) + ") "

    # remove duplicate and trailing spaces from name
    name = re.sub(' ,', ',', re.sub(' +', ' ', meal['name'].rstrip()))

    # format price with comma
    price = str(meal['prices'][args['price']]).replace('.',',') + " €"

    # build category string
    categories   = meal['category'].split()
    category_str = ''
    for category in set(categories):
        if category in category_map:
            category_str += category_map[category]
    # add brackets to category string if not empty
    if not category_str == '':
        category_str = ' [' + category_str + '] '
    else:
        category_str = ' '

    # print meal
    print(intent() + colorize(number + name + category_str + price, 'cyan'))

    i += 1

print()


# print legend
print(intent(), end='')
for category in category_map:
    print(colorize(category_map[category] + "=" + category, 'blue') + " ", end='')


# print xmas closing countdown (xmascc)
if not args['no_xmascc']:
    last_holiday = datetime.datetime.strptime(config.get('xmascc', 'last_holiday'), '%Y-%m-%d')
    last_workday = datetime.datetime.strptime(config.get('xmascc', 'last_workday'), '%Y-%m-%d')

    if date >= last_holiday and date.year == last_holiday.year:
        print("\n")
        print(intent(), end='')
        print(colorize(xmascc.get_countdown(date,last_workday), 'magenta'))


if not args['lite']: print("\n")
