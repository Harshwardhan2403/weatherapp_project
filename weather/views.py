from django.shortcuts import render

# Create your views here.
# weather/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer  # You will create this serializer next

class WeatherDataList(APIView):
    def get(self, request):
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)
