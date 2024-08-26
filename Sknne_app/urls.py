from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home),
    path('front_validation' , views.front_validation),
    path('signup' , views.signup),
    path('login' , views.login),
    path('cities' , views.cities),
    # path('rate_appartment', views.rate_appartment, name='rate_appartment'),
    path('clear-email-not-registered', views.clear_email_not_registered, name='clear_email_not_registered'),
    path('logout' , views.logout),
    path('city' , views.get_appartments),
    path('appartments' , views.show_appartments),
    path('<int:id>' , views.get_room),
    path('room' , views.show_room),
    path('email' , views.send_email),
]
