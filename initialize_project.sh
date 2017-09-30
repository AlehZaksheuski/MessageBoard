#!/bin/bash
sudo apt-get install virtualenv
sudo apt-get install python3
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py loaddata initial_data.json
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver