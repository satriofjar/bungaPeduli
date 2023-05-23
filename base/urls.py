from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list-donasi/', views.list_donasi, name='list-donasi'),
]