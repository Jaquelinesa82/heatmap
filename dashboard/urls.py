from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('data/all/', views.list_all_data),
    path('data/register/', views.register_data),
    path('data/register/submit', views.register_submit),
    path('', RedirectView.as_view(url='data/all/'))
]