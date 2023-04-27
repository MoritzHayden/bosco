#!/bin/bash

cd "$(dirname "$(readlink -f "$0")")/../src"
pip install --upgrade pip
pip install pipenv
pipenv install --dev
pipenv run python bot.py
