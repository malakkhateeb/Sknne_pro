from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('front_validation' , views.front_validation),
    path('signup' , views.signup),
    path('login' , views.login),
    path('cities' , views.cities),
    path('logout' , views.logout),
    path('city' , views.get_appartments),
    path('appartments' , views.show_appartments),
    path('<int:id>' , views.get_room),
    path('room' , views.show_room),
]