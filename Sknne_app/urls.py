from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home),
    path('front_validation' , views.front_validation),
    path('signup' , views.signup),
    path('login' , views.login),
    path('cities' , views.cities),
    path('clear-email-not-registered', views.clear_email_not_registered, name='clear_email_not_registered'),
    path('logout' , views.logout),
    path('city' , views.get_appartments),
    path('appartments' , views.show_appartments),
    path('<int:id>' , views.get_room),
    path('room' , views.show_room),
    path('email' , views.send_email),
    path('submit-rating', views.submit_rating, name='submit_rating'),
    path('about', views.about_us),
    path('submit_apartment' , views.submit_apartment),
    path('add_apartment' , views.add_appartment_owner),
    path('show-distance', views.show_distance)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

