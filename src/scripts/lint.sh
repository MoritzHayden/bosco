#!/bin/bash

cd "$(dirname "$(readlink -f "$0")")/.."
pip install --upgrade pip
pip install pipenv
pipenv install --dev
pipenv run pylint --rcfile .pylintrc **/*.py
