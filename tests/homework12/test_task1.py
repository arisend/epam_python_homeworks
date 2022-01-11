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
import homework_12_django.School.apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DJANGO_DIR = os.path.split(BASE_DIR)[0] + r'/homework_12_django'
sys.path.append(DJANGO_DIR)



#    Will try to complete in nearest future
# def test_migrations() -> None:
#     with open(DJANGO_DIR + '/test_main.db', 'w'): pass
#     dbs = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': DJANGO_DIR + "/test_main.db",
#         }
#     }
#
#     from django.conf import settings
#
#     settings.configure(
#         DATABASES=dbs,
#         INSTALLED_APPS=('School.apps.SchoolConfig',))  # add all the apps you need here
#     django.setup()
#
#     #from School.models import Homework
#
#
#
#     call_command('makemigrations', 'School')
#     call_command('migrate', '--noinput')
#
#     with open('test.json', "wb") as f:
#         management.call_command('dumpdata', stdout=f)
#     # for connection in connections.all():
#     #     connection.close()
#
#     with open('../../homework_12_django/initial_data.json', 'w') as initial_data_file:
#         with open('test.json', 'w') as test_file:
#             print(test_file.read())
#             print(initial_data_file.read())
#             assert json.load(initial_data_file) == json.load(test_file)
#     os.remove("test.json")
#     os.remove(DJANGO_DIR + "/test_main.db")

def test_report():
    dbs = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DJANGO_DIR + "/main.db",
        }
    }

    from django.conf import settings

    settings.configure(
        DATABASES=dbs,
        INSTALLED_APPS=('School.apps.SchoolConfig',))  # add all the apps you need here

    django.setup()

    from School.models import HomeworkResult


    result=[]
    for hwr in HomeworkResult.objects.filter(done=True).select_related('homework_id'):
        result.append([hwr.author,hwr.homework_id.created,hwr.homework_id.teacher])
    assert ['Lev Sokolov', datetime.datetime(2022, 1, 11, 4, 49, 25, 638826), 'Daniil Shadrin'] in result







