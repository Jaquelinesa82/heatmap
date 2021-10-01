from django.shortcuts import render, redirect
from .models import Data
import folium
from folium import plugins
import geocoder
# Create your views here.


def index(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude', 'population')

    map1 = folium.Map(location=[-18, -50], zoom_start=5)

    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)

    map1 = map1._repr_html_()
    context = {
        'map1': map1,
        'data_list': data
    }
    return render(request, 'dashboard/index.html', context=context)


def list_all_data(request):
    data = Data.objects.filter(active=True)
    return render(request, 'dashboard/index.html', {'data': data})


def register_data(request):
    return render(request, 'dashboard/register.html')


def register_submit(request):
    city = request.POST.get('city')
    population = request.POST.get('population')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    data = Data.objects.create(city=city, population=population, latitude=latitude, longitude=longitude)
    return redirect('/')
