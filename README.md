# canteenie

Small python script to get todays canteen/mensa meals for Friedrich-Alexander-University (FAU).

## Requirements

The following python 3 modules are needed:

* [requests](https://pypi.python.org/pypi/requests/2.11.1)
* [lxml](https://pypi.python.org/pypi/lxml/3.6.4)

### Installation

* Ubuntu/Debian: `$ apt-get install python3-requests python3-lxml`

## Usage

```
$ ./canteenie.py -h
usage: canteenie.py [-h] [-m {lmpl,sued,isch}] [-f]

Small python script to get todays canteen/mensa meals for FAU.

optional arguments:
  -h, --help            show this help message and exit
  -m {lmpl,sued,isch}, --mensa {lmpl,sued,isch}
                        for which mensa? (lmpl: Erlangen Langemarckplatz
                        (default), sued: Erlangen Süd, isch: Nürnberg Insel
                        Schütt)
  -f, --disable-figlet  disable figlet header

```
## Output example

```
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
