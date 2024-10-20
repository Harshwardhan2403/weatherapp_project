# weather/models.py

from django.db import models

class WeatherData(models.Model):
    date = models.DateField(unique=True)  # Store the date of the weather data
    tmax = models.FloatField(null=True, blank=True)  # Maximum temperature
    tmin = models.FloatField(null=True, blank=True)  # Minimum temperature
    rainfall = models.FloatField(null=True, blank=True)  # Total rainfall (if applicable)
    sunshine_duration = models.FloatField(null=True, blank=True)  # Total sunshine duration in hours

    def __str__(self):
        return f"Weather data for {self.date}: Tmax={self.tmax}, Tmin={self.tmin}"

    class Meta:
        verbose_name = "Weather Data"
        verbose_name_plural = "Weather Data"
