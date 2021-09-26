import folium
from django.shortcuts import render


def index(request):
    map1 = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)
    folium.Marker(location=[-15.7589665, -47.879422],
                  popup='Esplanada dos Ministerios',
                  icon=folium.Icon(color='red', icon='info-sign')
                  ).add_to(map1)
    map1 = map1._repr_html_()
    context = {
            'map1': map1
    }
    return render(request, 'dashboard/index.html', context)
