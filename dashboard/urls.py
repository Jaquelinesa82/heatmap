from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('data/all/', views.list_all_data),
]