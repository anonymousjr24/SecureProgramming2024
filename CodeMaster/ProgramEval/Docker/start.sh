#!/usr/bin/env bash

cd /code
python manage.py makemigrations
python manage.py migrate #Realiza los cambios

gunicorn --bind :8000 ProgramEval.wsgi:application --reload
#python manage.py runserver 0.0.0.0:8000