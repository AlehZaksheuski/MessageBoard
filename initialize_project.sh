#!/bin/bash
if ! [ "$1" = "--no-install" ]; then
    sudo apt-get install virtualenv
    sudo apt-get install python3
fi
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata --exclude=contenttypes --exclude=auth.Permission initial_data.json
python manage.py collectstatic --noinput
python manage.py runserver