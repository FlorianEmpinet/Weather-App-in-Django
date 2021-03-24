from django.shortcuts import render, redirect
import requests
# Create your views here.
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=fr&appid=YOUR_API_KEY'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    if (request.GET.get('DeleteButton')):
        City.objects.filter(name=request.GET.get('DeleteButton')).delete()
        return redirect('/')
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': round(r['main']['temp']),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)
