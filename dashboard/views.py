from django.shortcuts import render
from .models import Data
import folium
from folium import plugins
# Create your views here.


def index(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude', 'population')

    map1 = folium.Map(location=[-23, -50], zoom_start=5)

    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)

    map1 = map1._repr_html_()
    context = {
        'map1': map1
    }
    return render(request, 'dashboard/index.html', context)


def list_all_data(request):
    data = Data.objects.filter(active=True)
    return render(request, 'index.html', {'data': data})
