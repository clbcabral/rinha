#!/usr/bin/env sh
cd src
python manage.py migrate
gunicorn rinha.wsgi -b 0.0.0.0:8000
