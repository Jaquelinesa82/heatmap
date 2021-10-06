from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.listData, name='listData'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.update, name='delete'),
]