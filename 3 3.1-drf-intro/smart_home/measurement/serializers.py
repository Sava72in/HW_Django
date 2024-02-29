from rest_framework import serializers

from measurement.models import Sensor, Temperature_measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'descriptions']


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        temperature = Temperature_measurement
        fields = ['id', 'temperature', 'date', 'sensor']
