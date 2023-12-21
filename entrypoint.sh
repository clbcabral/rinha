#!/usr/bin/env sh
cd src
python manage.py migrate
mkdir -p /opt/app/logs
gunicorn rinha.wsgi --timeout 300 --error-logfile /opt/app/logs/gunicorn.log -b 0.0.0.0:8000