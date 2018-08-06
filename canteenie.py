#!/usr/bin/env python3

"""canteenie.py: A small python script that prints today's canteen/mensa menu for FAU on console."""

import requests
import datetime
import argparse
from lxml import html
from colorama import Fore, Style
import textwrap
import xmascc

# command line arguments
parser = argparse.ArgumentParser(description='A small python script that prints today\'s canteen/mensa menu for FAU on console.')
parser.add_argument('-m','--mensa', help='for which mensa? (lmpl: Erlangen Langemarckplatz (default), sued: Erlangen Süd, isch: Nürnberg Insel Schütt)', required=False, default="lmpl", choices=['lmpl', 'sued', 'isch'])
parser.add_argument('-l','--lite', help='disable ascii art header and color (lite view)', required=False, default=False, action='store_true')
args = vars(parser.parse_args())

# get html content from webpage
page = requests.get('http://www.werkswelt.de/?id=%s' %args['mensa'])
tree = html.fromstring(page.content)
menu = tree.xpath('/html/body/div[3]/div/div[2]/div[2]/text()')

# join to string and tidy up the text
menu_str = ' '.join(menu) # join list to one string
menu_str = menu_str.replace('\xa0', ' ') # remove no break space
menu_str = menu_str.replace('\n', ' ') # remove line feed
menu_str = menu_str.replace('\r', ' ') # remove carriage return
menu_str = " ".join(menu_str.split()) # remove more than one space

# count amount of meals
meal_count = menu_str.count("Essen")
meal_special_count = menu_str.count("Aktionsessen")

# print header
now = datetime.datetime.now()
if not args['lite']: print(Fore.YELLOW + '', end="")
if args['lite'] == False:
	print("\t                             ")
	print("\t __  __                      ")
	print("\t|  \/  | ___ _ __  ___  __ _ ")
	print("\t| |\/| |/ _ \ '_ \/ __|/ _` |")
	print("\t| |  | |  __/ | | \__ \ (_| |")
	print("\t|_|  |_|\___|_| |_|___/\__,_|")
	print("\t                             ")
if not args['lite']: print(Style.RESET_ALL + '', end="")

if not args['lite']: print(Fore.GREEN + '', end="")
if not args['lite']: print("\t", end='')
print("////////", now.strftime("%d.%m.%Y"),"/////////")
if not args['lite']: print(Style.RESET_ALL + '', end="")
print("")

def wrap(meal_string):
	prefix = "\t\t"
	preferredWidth = 105
	wrapper = textwrap.TextWrapper(subsequent_indent=prefix, width=preferredWidth)
	print(wrapper.fill(meal_string))
	return

# print normal meals
i = 1
while i < meal_count +1:
	if "Essen %d" %i in menu_str: # check for missing menu
		slice_amount = -8
		if "- €" in menu_str.split("Essen %d" %i,1)[1].split("(Gäste)",1)[0][:-8]: # check for missing price
			slice_amount = -5	

		if not args['lite']: print(Fore.CYAN + '', end="")
		if not args['lite']: print("\t", end='')
		meal_string = "%d\t" %i + menu_str.split("Essen %d" %i,1)[1].split("(Gäste)",1)[0][:slice_amount]
		if not args['lite']:
			wrap(meal_string)
		else:
			print(meal_string)
		if not args['lite']: print(Style.RESET_ALL + '', end="")
		i += 1
	else:
		meal_count += 1
		i += 1

# print special meals
if meal_special_count != 0:
	print("")
	i = 1
	while i < meal_special_count + 1:
		if "Aktionsessen %d" %i in menu_str: # check for missing menu
			slice_amount = -8
			if "- €" in menu_str.split("Aktionsessen %d" %i,1)[1].split("(Gäste)",1)[0][:-8]: # check for missing price
				slice_amount = -5
							
			if not args['lite']: print(Fore.BLUE + '', end="")
			if not args['lite']: print("\t", end='')
			meal_special_string= "A%d\t" %i + menu_str.split("Aktionsessen %d" %i,1)[1].split("(Gäste)",1)[0][:slice_amount]
			if not args['lite']:
				wrap(meal_special_string)
			else:
				print(meal_special_string)
			if not args['lite']: print(Style.RESET_ALL + '', end="")
			i += 1
		else:
			meal_special_count += 1
			i += 1
print("")
if not args['lite']: print("")

#xmascc
#if not args['lite']: print(Fore.MAGENTA + '', end="")
#if not args['lite']: print("\t", end='')
#print(xmascc.get_countdown())
#if not args['lite']: print(Style.RESET_ALL + '', end="")
#print("")
