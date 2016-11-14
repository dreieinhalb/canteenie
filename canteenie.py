#!/usr/bin/env python3

"""canteenie.py: Small python script to get todays canteen/mensa meals for FAU."""

import requests
import datetime
import argparse
import pyfiglet
from lxml import html
from lxml import etree
from lxml.etree import tostring

# command line arguments
parser = argparse.ArgumentParser(description='Small python script to get todays canteen/mensa meals for FAU.')
parser.add_argument('-m','--mensa', help='for which mensa? (lmpl: Erlangen Langemarckplatz (default), sued: Erlangen Süd, isch: Nürnberg Insel Schütt)', required=False, default="lmpl", choices=['lmpl', 'sued', 'isch'])
parser.add_argument('-f','--disable-figlet', help='disable figlet header', required=False, default=False, action='store_true')
args = vars(parser.parse_args())

# get html content from webpage
page = requests.get('http://www.werkswelt.de/?id=%s' %args['mensa'])
tree = html.fromstring(page.content)
menu = tree.xpath('/html/body/div[3]/div/div[2]/div[2]/text()')

# join to string and tidy up the text
menu_str = ' '.join(menu) # join list to one string
menu_str = menu_str.replace(u'\xa0', u' ') # remove no break space
menu_str = menu_str.replace(u'\n', u' ') # remove line feed
menu_str = menu_str.replace(u'\r', u' ') # remove carriage return
menu_str = " ".join(menu_str.split()) # remove more than one space

# count amount of meals
meal_count = menu_str.count("Essen")
meal_special_count = menu_str.count("Aktionsessen")

# print header
now = datetime.datetime.now()
if args['disable_figlet'] == False:
	pyfiglet.print_figlet("Mensa")
print("////////", now.strftime("%d.%m.%Y"),"/////////")
print("")

# print normal meals
for i in range(1, meal_count + 1):
	print("%d  " %i, menu_str.split("Essen %d" %i,1)[1].split("(Gäste)",1)[0][:-8])

# print special meals
if meal_special_count != 0:
	print("")
	for i in range(1, meal_special_count + 1):
		print("A%d " %i, menu_str.split("Aktionsessen %d" %i,1)[1].split("(Gäste)",1)[0][:-8])

print("")
