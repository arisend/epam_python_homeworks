from django.shortcuts import render
from .models import WWOnlineTable
import os
from datetime import date
import pandas as pd
import numpy as np
import sys


def sum_two_angles(first_angle, second_angle):
    """This auxiliary function sums two angles specified in degrees"""
    max_v = max(first_angle, second_angle)
    min_v = min(first_angle, second_angle)
    if max_v - min_v >= 180:
        result_angle = (max_v - 360 + min_v) / 2
        if result_angle < 0:
            result_angle = result_angle + 360
    else:
        result_angle = (max_v + min_v) / 2
    return result_angle


def get_data_from_db_and_analyze(location, start, end):
    """ This function connect to db, retrieve data for specified location and dates
    and conduct basic analysis using pandas tool set"""
    result = []
    resultdict = {}
    for row in WWOnlineTable.objects.filter(location=location,
                                            date_time__range=(start, end)).all():
        result.append([row.maxtempC, row.mintempC, row.winddirDegree, row.windspeedKmph, row.location, row.cloudcover,
                       row.totalSnow_cm, row.precipMM, row.date_time])
    df = pd.DataFrame(result,
                      columns=['maxtempC', 'mintempC', 'winddirDegree', 'windspeedKmph', 'location', 'cloudcover',
                               'totalSnow_cm', 'precipMM', 'date_time'])
    resultdict['abs_min'] = df['mintempC'].min()
    resultdict['abs_max'] = df['maxtempC'].max()
    resultdict['avereg'] = round((df['maxtempC'].mean() + df['mintempC'].mean()) / 2, 2)

    df['date_time_obj'] = pd.to_datetime(df['date_time'])

    if (end - start).days > 730:
        dfyearaverages = df[['maxtempC', 'mintempC', 'date_time_obj']].groupby(
            pd.Grouper(key='date_time_obj', freq='Y')).mean().round(2)
        dfyearaverages['year'] = dfyearaverages.index.year
        by_column = [dfyearaverages[x].values.tolist() for x in dfyearaverages.columns]
        resultdict['dfyearaverages'] = list(list(x) for x in zip(*by_column))
    else:
        resultdict['dfyearaverages'] = None

    df['type_of_precipitation'] = np.where(df['totalSnow_cm'] != 0, 'snow',
                                           np.where(df['precipMM'] != 0, 'rain', ""))
    for type_of_precipitation in df['type_of_precipitation'].value_counts().index:
        if type_of_precipitation != "":
            resultdict['type_of_precipitation'] = type_of_precipitation
            break

    resultdict['avgwindspeed'] = round(df['windspeedKmph'].mean(), 2)

    sum_angle = None
    for i in df['winddirDegree']:
        if not sum_angle:
            sum_angle = i
        else:
            sum_angle = sum_two_angles(sum_angle, i)
    resultdict['sum_angle'] = round(sum_angle, 2)

    df['cloud'] = np.where(df['cloudcover'] > 75, 'clouds', np.where(df['cloudcover'] < 75, 'sunny', ""))
    df['weather_tag'] = df['cloud'] + " " + df['type_of_precipitation']
    for weather_tag in df['weather_tag'].value_counts().index:
        if weather_tag != '':
            resultdict['weather_tag'] = weather_tag
            break
    return resultdict


def weather_create_view(request):
    """This django view hols all the logic of web page"""
    context = {}
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    cities_path = os.path.join(BASE_DIR, 'list_of_cities.txt')
    with open(cities_path) as f:
        list_of_cities = f.read().splitlines()
    context['cities'] = list_of_cities

    if request.method == "POST":
        try:
            from datetime import datetime
            start = datetime.strptime(request.POST.get('period-start'), '%Y-%m-%d').date()
            end = datetime.strptime(request.POST.get('period-end'), '%Y-%m-%d').date()
            if request.POST.get('location') in list_of_cities and \
                    date(2010, 1, 1) <= start <= end <= datetime.now().date():
                context['wrong_dates'] = False
                location = request.POST.get('location')
                context['period_start'] = request.POST.get('period-start')
                context['period_end'] = request.POST.get('period-end')
                context['location'] = location
                context.update(get_data_from_db_and_analyze(location, start, end))
            else:
                context['wrong_dates'] = True

        except TypeError as err:
            context['wrong_dates'] = True

    return render(request, 'weather_page/weather_create.html', context)
