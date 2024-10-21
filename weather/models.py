# weather/models.py

from django.db import models

class WeatherData(models.Model):
    date = models.DateField(unique=True)  
    tmax = models.FloatField(null=True, blank=True)  
    tmin = models.FloatField(null=True, blank=True)  
    rainfall = models.FloatField(null=True, blank=True)  
    sunshine_duration = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return f"Weather data for {self.date}: Tmax={self.tmax}, Tmin={self.tmin}"

    class Meta:
        verbose_name = "Weather Data"
        verbose_name_plural = "Weather Data"
