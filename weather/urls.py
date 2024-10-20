from django.urls import path
from .views import WeatherDataList

urlpatterns = [
    path('api/weather/', WeatherDataList.as_view(), name='weather-data-list'),
]