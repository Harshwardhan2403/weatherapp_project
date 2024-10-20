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

        # Print the response for debugging
        print("Response data:", data)

        # Update within your loop in fetch_weather_data.py

for line in data[1:]:  # type: ignore # Skip the header line
    parts = line.split()

    # Check for enough parts
    if len(parts) < 3:
        print("Skipping line due to insufficient parts:", line)
        continue

    # Extract date
    raw_date = parts[0]
    
    # Example logic to convert a year to a full date
    if len(raw_date) == 4:  # Assuming it's just the year
        date = f"{raw_date}-01-01"  # Default to January 1st
    else:
        date = raw_date  # or handle differently if it's a different format

    print("Parsed date:", date)  # Debugging output

    try:
        tmax = float(parts[1])
        tmin = float(parts[2])
    except ValueError as e:
        print("Error converting to float:", e, "for line:", line)
        continue

    # Save data to the database
    WeatherData.objects.create(date=date, tmax=tmax, tmin=tmin)
