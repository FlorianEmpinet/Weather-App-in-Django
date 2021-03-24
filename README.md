# Weather App

Weather App is a simple Django/ Python app to check the weather in a city.

## Installation

Clone this repo

Migrate the database : 

```bash
python manage.py migrate
```

Get an API key on : [OpenWeatherMap](https://openweathermap.org/api)

Change the API KEY in : 

Weather Folder | views.py | url

```bash
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=fr&appid=YOUR_API_KEY'
```
And it's ready ! 

```bash
python3.9 manage.py runserver
```

[127.0.0.1:8000/](http://127.0.0.1:8000/)
## Configurations

I use Django 3.0.8 & Python 3.9.2 
