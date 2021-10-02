from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.listData, name='listData'),
    path('createData/', views.createData, name='createData'),
]