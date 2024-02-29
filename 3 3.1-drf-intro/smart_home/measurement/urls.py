from django.urls import path

from measurement.views import Get_temp, Sensor_View, Modify_sensor, Modify_data

urlpatterns = [
    path('get_temp/', Get_temp.as_view()),
    path('sensor/<pk>/', Sensor_View.as_view()),
    path('modify/<pk>/', Modify_sensor.as_view()),
    path('modify_temp/<pk>/', Modify_data.as_view()),

]
