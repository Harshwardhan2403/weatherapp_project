# weather/management/commands/fetch_weather_data.py

import requests
from django.core.management.base import BaseCommand
from weather.models import WeatherData

class Command(BaseCommand):
    help = 'Fetch weather data from the UK MetOffice'

    def handle(self, *args, **kwargs):
        url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"
        
        response = requests.get(url)
        data = response.text.splitlines()

        print("Response data:", data)

for line in data[1:]: 
    parts = line.split()

   
    if len(parts) < 3:
        print("Skipping line due to insufficient parts:", line)
        continue

    
    raw_date = parts[0]
    
   
    if len(raw_date) == 4:  
        date = f"{raw_date}-01-01"  
    else:
        date = raw_date  

    print("Parsed date:", date)  

    try:
        tmax = float(parts[1])
        tmin = float(parts[2])
    except ValueError as e:
        print("Error converting to float:", e, "for line:", line)
        continue
    
    WeatherData.objects.create(date=date, tmax=tmax, tmin=tmin)
