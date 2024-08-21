from django.urls import path
from . import views

urlpatterns = [
    path('', views.logIn),
    path('front_validation' , views.front_validation),
    path('signup' , views.signup),
    path('login' , views.login),
    path('city', views.city)
]