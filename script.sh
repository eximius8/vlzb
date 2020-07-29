#!/bin/bash
rm -rf .env/
python3 -m venv .env
source .env/bin/activate
pip install -U pip
pip install -r requirements.txt
pip install django-debug-toolbar
pip install django-bleach
python manage.py runserver
