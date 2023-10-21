from django.urls import path
from .views import SensorsView, SensorView, SensorDeleteView, MeasurementsAddView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<id>/', SensorView.as_view()),
    path('measurements/', MeasurementsAddView.as_view()),
    path('sensor_delete/<id>/', SensorDeleteView.as_view()),
]
