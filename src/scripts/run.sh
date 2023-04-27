#!/bin/bash

cd "$(dirname "$(readlink -f "$0")")/.."
pip install --upgrade pip
pip install pipenv
pipenv install
pipenv run python bot.py
