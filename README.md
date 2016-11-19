# canteenie

Small python script to get todays canteen/mensa meals for Friedrich-Alexander-University (FAU).

## Requirements

The following python 3 modules are needed:

* [requests](https://pypi.python.org/pypi/requests/2.11.1) (ubuntu/debian package name: python3-requests)
* [lxml](https://pypi.python.org/pypi/lxml/3.6.4) (ubuntu/debian package name: python3-lxml)

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
