import os
import sys
import django
import datetime
from django.db.models import Max

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DJANGO_DIR = os.path.split(BASE_DIR)[0] + r'/weather_page'
sys.path.append(DJANGO_DIR)
print(DJANGO_DIR)
print(BASE_DIR)

dbs = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DJANGO_DIR, r'db.sqlite3')
    }
}
cities_path = os.path.join(DJANGO_DIR, r'list_of_cities.txt')
with open(cities_path) as f:
    location_list = f.read().splitlines()

settings.configure(
    DATABASES=dbs,
    INSTALLED_APPS=('weather_history','weather_page'), ROOT_URLCONF = 'weather_page.weather_history.urls', SECRET_KEY = 'django-insecure-73+82eiear69!ctao$47j$h579bd0v00z4!ph6s8j$tz0anv*w',TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.path.join(DJANGO_DIR, r'templates'),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]),

django.setup()
from django.contrib import admin
from django.urls import include,path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path

from weather_page.weather_history import views,urls

urlpatterns = [
    path('', views.weather_create_view, name='create'),
]

urlpatterns += staticfiles_urlpatterns('/')
from weather_page.weather_history.models import *

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# DJANGO_DIR = os.path.split(BASE_DIR)[0] + r'/weather_page'
# sys.path.append(DJANGO_DIR)
#
# dbs = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, r'..\weather_page\db.sqlite3')
#     }
# }
# cities_path = os.path.join(BASE_DIR, r'..\weather_page\list_of_cities.txt')
# with open(cities_path) as f:
#     location_list = f.read().splitlines()
#
# settings.configure(
#     DATABASES=dbs,
#     INSTALLED_APPS=('weather_history.apps.WeatherHistoryConfig',))
# django.setup()
# from weather_page.weather_history.models import WWOnlineTable
# WWOnlineTable.objects.aggregate(Max('date_time'))['date_time__max']

#
# from django.test.utils import setup_test_environment
# setup_test_environment(c)
from django.test import Client
client = Client()
response = client.get('/')
print(response.status_code)
print(response.content)
print(response.context['location'])