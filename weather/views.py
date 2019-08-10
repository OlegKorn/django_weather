from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):

    appid = '0b005ff217784d85c005f7c4bac2d02f'  # https://home.openweathermap.org/api_keys
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm() 

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_info = {
            'city' : city.name,
            'temp' : r['main']['temp'],
            'icon' : r['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info' : all_cities, 'form' : form}

    return render(request, 'weather/index.html', context)
