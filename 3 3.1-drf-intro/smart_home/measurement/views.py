# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Temperature_measurement
from .serializers import SensorSerializer, TempSerializer


class Get_temp(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        name = self.request.GET.get('name')
        descriptions = self.request.GET.get('descriptions')
        Sensor(name=name, descriptions=descriptions).save()
        return Response({'status': 'OK'})


class Sensor_View(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Modify_sensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Modify_data(UpdateAPIView):
    queryset = Temperature_measurement.objects.all()
    serializer_class = TempSerializer




