# Leerstandsmelder Django Demo

## Requirements

- python 3
- virtualenv
- virtualenvwrapper


## Installation

    mkvirtualenv -p /usr/bin/python3 leerstandsmelder
    pip install ipython zc.buildout
    buildout -Nv

## Initialization

The django manage commands are executed via bin/development created by buildout

initialize database

    bin/development migrate

create super user

    bin/development createsuperuser

import data from original leerstandsmelder

    bin/development initial_import

start development server

    bin/development runserver

