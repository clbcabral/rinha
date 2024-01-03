#!/usr/bin/env sh
cd src
gunicorn -b 0.0.0.0 'app:app'