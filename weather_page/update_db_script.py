import os
import sys
import django
import datetime
from django.db.models import Max
from wwo_hist import retrieve_hist_data
from django.conf import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

dbs = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, r'app/db.sqlite3')
    }
}
cities_path = os.path.join(BASE_DIR, r'app/list_of_cities.txt')
with open(cities_path) as f:
    location_list = f.read().splitlines()

settings.configure(
    DATABASES=dbs,
    INSTALLED_APPS=('weather_history.apps.WeatherHistoryConfig',))
django.setup()
from weather_history.models import *

def upload_data_to_db():
    """This function open connection to db, check the latest available weather and parse api.worldweatheronline.com
     for new data. At the last step it stores new data to db"""

    def get_last_date():
        return WWOnlineTable.objects.aggregate(Max('date_time'))['date_time__max']
    print(get_last_date())
    frequency = 24
    start_date = get_last_date()
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    api_key = 'f3b863482ce74cb5828172003221801'
    dflist = retrieve_hist_data(api_key, location_list,
                                           start_date,
                                           end_date,
                                           frequency,
                                           location_label=False,
                                           export_csv=False,
                                           store_df=True)

    for city in dflist:
        for index, row in city.iterrows():
            datestr=row['date_time'].strftime("%Y-%m-%d")
            new_row = WWOnlineTable(mintempC=row['mintempC'],
                                    maxtempC=row['maxtempC'],
                                    winddirDegree=row['winddirDegree'],
                                    windspeedKmph=row['windspeedKmph'],
                                    location=row['location'],
                                    cloudcover=row['cloudcover'],
                                    totalSnow_cm=row['totalSnow_cm'],
                                    precipMM=row['precipMM'],
                                    date_location=F"{datestr}|{row['location']}",
                                    date_time=row['date_time'])
            new_row.save()

if __name__ == '__main__':
    upload_data_to_db()

