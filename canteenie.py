#!/usr/bin/env python3

import re
import datetime
from openmensa import OpenMensa as OM

now = datetime.datetime.now()

#meals = OM.get_meals_by_day(264, now.strftime("%Y-%m-%d"))

for x in range(6,9):
    meals = OM.get_meals_by_day(264, "2018-08-0%d" %x)

    i = 1;
    for meal in meals:
        name = re.sub(' ,', ',', re.sub(' +', ' ', meal['name'].rstrip()))
        price = str(meal['prices']['employees']).replace('.',',')

        if meal['category'] == 'Vegetarisch':
            print("%d." %i, name, "[V]", price, "€")
        else:
            print("%d." %i, name, price, "€")

        i += 1

    print(" ")
