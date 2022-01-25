from django.test import TestCase

# Create your tests here.
import os
import sys
import django
import datetime
from django.db.models import Max
from wwo_hist import retrieve_hist_data
from django.conf import settings
from weather_history.models import *
from django.test import Client


class TestModels(TestCase):
    def test_add_rows_to_db(self):
        row1=WWOnlineTable.objects.create(date_time='2100-01-01', location='Rostov-on-Don', date_location='Rostov-on-Don|2100-01-01', maxtempC=0, mintempC=0, winddirDegree=0, windspeedKmph=0, cloudcover=0, totalSnow_cm=0, precipMM=0)
        row2 = WWOnlineTable.objects.create(date_time='2100-01-02', location='Rostov-on-Don',
                                            date_location='Rostov-on-Don|2100-01-02',maxtempC=0, mintempC=0, winddirDegree=0, windspeedKmph=0, cloudcover=0, totalSnow_cm=0, precipMM=0)
        print(WWOnlineTable.objects.filter(date_time__year__gte=2099).count())
        self.assertEqual(WWOnlineTable.objects.filter(date_time__year__gte=2099).count(), 2)


class TestForm(TestCase):
    def test_can_send_message(self):
        c = Client()
        data = {
            "location": "Riga",
            "start": " 2010-01-01",
            "end": "2010-01-02",
        }
        response = c.post('', data)
        self.assertTemplateUsed(response, "weather_page/weather_create.html")
        self.assertContains(response,"location")
        self.assertContains(response, "start")

