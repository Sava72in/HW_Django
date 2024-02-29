import datetime

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=50)


class Temperature_measurement(models.Model):
    temperature = models.IntegerField()
    date = models.DateField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')
