from django.urls import path

from .views import SensorListView, MeasurementListCreateView, SensorRetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementListCreateView.as_view()),

]
