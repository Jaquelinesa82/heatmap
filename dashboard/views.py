from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
import folium
from folium import plugins


def listData(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude', 'population')

    map1 = folium.Map(location=[-18, -50], zoom_start=2)

    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)

    map1 = map1._repr_html_()
    context = {
        'map1': map1,
        'data_list': data
    }
    return render(request, 'dashboard/index.html', context=context)


def createData(request):
    form = DataForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'dashboard/dataForm.html', {'form': form})
