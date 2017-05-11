# Leerstandsmelder Django Demo

## Requirements

- python 3
- python 3 headers
- libjpeg headers,
- zlib headers
- virtualenv
- virtualenvwrapper


    apt-get install python3-dev libjpeg-dev zlib1g-dev python3-virtualenv


## Installation

    mkvirtualenv -p /usr/bin/python3 leerstandsmelder
    pip install ipython zc.buildout
    buildout -Nv

Sometimes problems with pip and setuptools prevent the installation

    pip uninstall setuptools
    pip install setuptools
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
