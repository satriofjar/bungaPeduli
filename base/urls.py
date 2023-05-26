from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donasi/', views.list_donasi, name='list-donasi'),
    path('kategori/', views.kategori, name='kategori'),
    path('galang-dana/', views.form_galang_dana, name='form-galang-dana'),
    path('donasi/<str:pk>/', views.donasi, name='donasi'),
    path('form-donasi/<str:pk>', views.form_donation, name='form-donasi'),
    path('payment-success/<str:pk1>/<str:pk2>', views.payment_success, name='payment'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_page, name='register'),
]