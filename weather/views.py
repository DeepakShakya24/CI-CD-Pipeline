from django.shortcuts import render
import urllib.request
import requests
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        params = {
            'access_key': 'a9f8f8ab12c0b6bb34cfda170721af2e',
            'query': city
        }
        source = requests.get('http://api.weatherstack.com/current', params)

        # converting JSON data to a dictionary
        r = source.json()
        city_weather={
            'city': str(city),
            'country': str(r['location']['country']),
            'time': str(r['location']["localtime"]),
            'temperature': str(r['current']['temperature']),
            'description': str(r['current']['weather_descriptions'][0]),
            'icon': r['current']['weather_icons'][0]
        }

        print(city_weather)
    else:
        city_weather={}
    return render(request,'weather/weather.html',city_weather)