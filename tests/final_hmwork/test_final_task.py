from django.core.management import call_command
from django.db import connections
from django.conf import settings
import os
import sys
import django
import csv
import json
import datetime
import os.path
from django.core import management
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DJANGO_DIR = os.path.split(BASE_DIR)[0] + r'/weather_page'
sys.path.append(DJANGO_DIR)



def test_report():
    dbs = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, r'weather_page\db.sqlite3')
        }
    }

    from django.conf import settings

    settings.configure(
        DATABASES=dbs,
        INSTALLED_APPS=('weather_history.apps.WeatherHistoryConfig',))
    django.setup()
    from weather_page.weather_history.models import *




    result=[]
    for hwr in HomeworkResult.objects.filter(done=True).select_related('homework_id'):
        result.append([hwr.author,hwr.homework_id.created,hwr.homework_id.teacher])
    assert ['Lev Sokolov', datetime.datetime(2022, 1, 11, 4, 49, 25, 638826), 'Daniil Shadrin'] in result