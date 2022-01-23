from django.db import models

# Create your models here.



class WWOnlineTable(models.Model):
    date_time = models.DateField('date collected')
    location = models.CharField(max_length=50)
    date_location= models.CharField(max_length=100, primary_key=True)
    maxtempC=models.FloatField()
    mintempC=models.FloatField()
    winddirDegree = models.IntegerField()
    windspeedKmph=models.FloatField()
    cloudcover =models.IntegerField()
    totalSnow_cm =models.FloatField()
    precipMM =models.FloatField()



