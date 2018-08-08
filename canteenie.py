#!/usr/bin/env python3

"""canteenie.py: A small python script that prints today's canteen/mensa on console using openmensa API."""

import argparse
import datetime
from openmensa import OpenMensa as openmensa
import re
from termcolor import colored

# function to validate date
def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

# function to return colored text
def colorize(text, color):
    # only return colored text if lite option is not set
    if not args['lite']:
        return colored(text, color)
    else:
        return text

# function to return intentation
def intent():
    # only return intentation if lite option is not set
    if not args['lite']:
        return "\t"
    else:
        return ''

# command line arguments
parser = argparse.ArgumentParser(description='A small python script that prints today\'s canteen/mensa menu for FAU on console.')
parser.add_argument(
        '-m',
        '--mensa',
        help='for which mensa? (lmpl: Erlangen Langemarckplatz (default), sued: Erlangen Süd, isch: Nürnberg Insel Schütt)',
        choices=['lmpl', 'sued', 'isch'],
        default="lmpl",
        required=False
)
parser.add_argument(
        '-i',
        '--id',
        help='for which ID on openmensa.org?',
        default=argparse.SUPPRESS, # don't define key if not given
        required=False
)
parser.add_argument(
        '-d',
        '--date',
        help='for which date (YYYY-MM-DD)?',
        default=argparse.SUPPRESS, # don't define key if not given
        required=False,
        type=valid_date
)
parser.add_argument(
        '-l',
        '--lite',
        help='disable ascii art header and color (lite view)',
        action='store_true',
        default=False,
        required=False
)
parser.add_argument(
        '-p',
        '--price',
        help='prices for which group? (employees (default), students, others)',
        choices=['employees', 'students', 'others'],
        default="employees",
        required=False
)
args = vars(parser.parse_args())

# map for assignment of IDs for FAU canteens
fau_mensa = {"lmpl":264, "sued":256, "isch":265}

# use mensa Langemarckplatz as default, or use given ID from args
openmensa_id = 264
if 'mensa' in args:
    openmensa_id = fau_mensa[args['mensa']]
if 'id' in args:
    openmensa_id = args['id']

# use today as default or given date from args
date = datetime.datetime.now()
if 'date' in args:
    date = args['date']

# get meals from openmensa API
meals = openmensa.get_meals_by_day(openmensa_id, date.strftime("%Y-%m-%d"))

# print header (ascii art only in non lite version)
if not args['lite']:
    print(intent() + colorize("                              ",'yellow'))
    print(intent() + colorize("  __  __                      ",'yellow'))
    print(intent() + colorize(" |  \/  | ___ _ __  ___  __ _ ",'yellow'))
    print(intent() + colorize(" | |\/| |/ _ \ '_ \/ __|/ _` |",'yellow'))
    print(intent() + colorize(" | |  | |  __/ | | \__ \ (_| |",'yellow'))
    print(intent() + colorize(" |_|  |_|\___|_| |_|___/\__,_|",'yellow'))
    print(intent() + colorize("                              ",'yellow'))
print(intent() + colorize("//////// " + date.strftime("%d.%m.%Y") + " /////////", 'green'))
print("")

# map for assignment of categories to abbreviations
category_map = {"Vegetarisch":"V", "Schwein":"S", "Rind":"R", "Geflügel":"G", "Fisch":"F"}

# set counter for numbering meals
i = 1;
for meal in meals:
    number = "(" + str(i) + ") "
    # remove duplicate and trailing spaces from name
    name = re.sub(' ,', ',', re.sub(' +', ' ', meal['name'].rstrip()))
    # format price with comma
    price = str(meal['prices'][args['price']]).replace('.',',') + " €"
    # build category string
    categories = meal['category'].split()
    category_str = ''
    for category in categories:
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
print("\n")
