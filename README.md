![canteenie logo](/icon/canteenie_logo.png)

# canteenie

A small python script that prints today's canteen/mensa on console using openmensa API.

## Requirements

The following python 3 modules are needed:

* [termcolor](https://pypi.org/project/termcolor/)
* [openmensa-api](https://github.com/brennerm/openmensa-api)

## Installation

* Install modules on Ubuntu/Debian: `$ apt-get install python3-termcolor`
* Install openmensa-api with pip: `$ pip3 install openmensa-api`
* Clone this git repository: `$ git clone https://github.com/dreieinhalb/canteenie.git`

## Usage

```
$ ./canteenie.py -h
usage: canteenie.py [-h] [-m {lmpl,sued,isch}] [-i ID] [-d DATE] [-l]
                    [-p {employees,students,others}]

A small python script that prints today's canteen/mensa menu for FAU on
console.

optional arguments:
  -h, --help            show this help message and exit
  -m {lmpl,sued,isch}, --mensa {lmpl,sued,isch}
                        for which mensa? (lmpl: Erlangen Langemarckplatz
                        (default), sued: Erlangen Süd, isch: Nürnberg Insel
                        Schütt)
  -i ID, --id ID        for which ID on openmensa.org?
  -d DATE, --date DATE  for which date (YYYY-MM-DD)?
  -l, --lite            disable ascii art header and color (lite view)
  -p {employees,students,others}, --price {employees,students,others}
                        prices for which group? (employees (default),
                        students, others)
```

## Output example

```
$ ./canteenie.py
                                     
         __  __                      
        |  \/  | ___ _ __  ___  __ _ 
        | |\/| |/ _ \ '_ \/ __|/ _` |
        | |  | |  __/ | | \__ \ (_| |
        |_|  |_|\___|_| |_|___/\__,_|
                                     
        //////// 08.08.2018 /////////

        (1) Maultaschen mit Gemüse-Füllung auf Ratatouille [V] 3,23 €
        (2) Pizza Vier Käse [V] 4,33 €
        (3) Apfel-Nuss Couscous mit lackierten Hähnchenbruststreifen [G] 3,38 €
        (4) Seehecht m. Schwarzwurzelragout u. Bandnudeln [VF] 4,89 €
        (5) Pizza Speziale [SG] 4,99 €

        V=Vegetarisch S=Schwein R=Rind G=Geflügel F=Fisch 

```
