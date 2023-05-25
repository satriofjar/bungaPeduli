from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list-donasi/', views.list_donasi, name='list-donasi'),
    path('kategori/', views.kategori, name='kategori'),
    path('galang-dana/', views.form_galang_dana, name='form-galang-dana'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_page, name='register'),
]