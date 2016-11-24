#!/usr/bin/env python3

"""canteenie.py: A small python script that prints today's canteen/mensa menu for FAU on console."""

import requests
import datetime
import argparse
from lxml import html

# command line arguments
parser = argparse.ArgumentParser(description='A small python script that prints today\'s canteen/mensa menu for FAU on console.')
parser.add_argument('-m','--mensa', help='for which mensa? (lmpl: Erlangen Langemarckplatz (default), sued: Erlangen Süd, isch: Nürnberg Insel Schütt)', required=False, default="lmpl", choices=['lmpl', 'sued', 'isch'])
parser.add_argument('-l','--disable-header', help='disable ascii art header (lite view)', required=False, default=False, action='store_true')
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
if args['disable_header'] == False:
	print(" __  __                      ")
	print("|  \/  | ___ _ __  ___  __ _ ")
	print("| |\/| |/ _ \ '_ \/ __|/ _` |")
	print("| |  | |  __/ | | \__ \ (_| |")
	print("|_|  |_|\___|_| |_|___/\__,_|")
	print("                             ")

print("////////", now.strftime("%d.%m.%Y"),"/////////")
print("")

# print normal meals
i = 1
while i < meal_count +1:
	if "Essen %d" %i in menu_str: # check for missing menu
		slice_amount = -8
		if "- €" in menu_str.split("Essen %d" %i,1)[1].split("(Gäste)",1)[0][:-8]: # check for missing price
			slice_amount = -5	

		print("%d  " %i, menu_str.split("Essen %d" %i,1)[1].split("(Gäste)",1)[0][:slice_amount]) # print meal
		i += 1
	else:
		print("A%d " %i, "-") # print pace holder
		if meal_count < menu_str.count("Essen"): # check for two meals with same number
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
							
			print("A%d " %i, menu_str.split("Aktionsessen %d" %i,1)[1].split("(Gäste)",1)[0][:slice_amount]) # print meal
			i += 1
		else:
			print("A%d " %i, "-") # print pace holder
			if meal_special_count < menu_str.count("Aktionsessen"): # check for two meals with same number
				meal_special_count += 1
			i += 1
print("")
