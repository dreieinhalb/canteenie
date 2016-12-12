![canteenie logo](/icon/canteenie_logo.png)

# canteenie

A small python script that prints today's canteen/mensa menu for Friedrich-Alexander-University (FAU) on console.

## Requirements

The following python 3 modules are needed:

* [requests](https://pypi.python.org/pypi/requests)
* [lxml](https://pypi.python.org/pypi/lxml)
* [colorama](https://pypi.python.org/pypi/colorama)

## Installation

* Install modules on Ubuntu/Debian: `$ apt-get install python3-requests python3-lxml python3-colorama`
* Clone git repository: `$ git clone https://github.com/dreieinhalb/canteenie.git`

## Usage

```
$ ./canteenie.py -h
usage: canteenie [-h] [-m {lmpl,sued,isch}] [-l]

A small python script that prints today's canteen/mensa menu for FAU on
console.

optional arguments:
  -h, --help            show this help message and exit
  -m {lmpl,sued,isch}, --mensa {lmpl,sued,isch}
                        for which mensa? (lmpl: Erlangen Langemarckplatz
                        (default), sued: Erlangen Süd, isch: Nürnberg Insel
                        Schütt)
  -l, --lite            disable ascii art header and color (lite view)
```

## Output example

```
$ ./canteenie.py
 __  __
|  \/  | ___ _ __  ___  __ _
| |\/| |/ _ \ '_ \/ __|/ _` |
| |  | |  __/ | | \__ \ (_| |
|_|  |_|\___|_| |_|___/\__,_|

//////// 19.11.2016 /////////

1   Hähnchen Nuggets mit Salsa - Dip 2,39 € (Stud.) 3,39 € (Bed.)
2   Maultaschen vegetarisch mit Kräutersoße 1,88 € (Stud.) 2,88 € (Bed.)

A1  Nudelpfanne mit Zucch.,Staudensell.,Papr.,Radicchio,Reibekäs 1,98 € (Stud.) 2,98 € (Bed.)
A2  Hähnchenbrustfilet mit Zwiebel-Käsetopping Rahmsoße Spätzle - € (Stud.) - € (Bed.)
A3  Pizza Grillia, vegetarisch 3,33 € (Stud.) 4,33 € (Bed.)
A4  Pizza Diabolo 3,99 € (Stud.) 4,99 € (Bed.)

```
