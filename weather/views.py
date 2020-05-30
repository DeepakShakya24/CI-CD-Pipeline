from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=fd101856268b92f37fcb9280a3235743').read()
        r = json.loads(source)
        city_weather={
                'city':city,
                'temperature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon']
        }

        print(city_weather)
    else:
        city_weather={}
    return render(request,'weather/weather.html',city_weather)