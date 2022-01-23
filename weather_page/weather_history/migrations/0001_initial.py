# Generated by Django 4.0.1 on 2022-01-19 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WWOnlineTable',
            fields=[
                ('date_time', models.DateField(verbose_name='date collected')),
                ('location', models.CharField(max_length=50)),
                ('date_location', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('maxtempC', models.FloatField()),
                ('mintempC', models.FloatField()),
                ('winddirDegree', models.IntegerField()),
                ('windspeedKmph', models.FloatField()),
                ('cloudcover', models.IntegerField()),
                ('totalSnow_cm', models.FloatField()),
                ('precipMM', models.FloatField()),
            ],
        ),
    ]
