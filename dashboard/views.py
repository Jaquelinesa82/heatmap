from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
        'data_list': data,
    }
    return render(request, 'dashboard/index.html', context)


def create(request):
    form = DataForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'dashboard/create.html', {'form': form})


def update(request, id):
    data = Data.objects.get(id=id)
    form = DataForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('listData')
    return render(request, 'dashboard/update.html', {'data': data})


def delete(request, id):
    data = Data.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('listData')
