from django.urls import path
from django.contrib import admin
from .  import views


urlpatterns = [
    path('', views.home, name="home"),
    # Project Urls
    path('aboutus/',views.aboutus, name="aboutus"),
    path('blog/', views.blog, name = "blog"),
    path('concert/', views.concert, name='concert'),
    path('contact/', views.contact, name='contact'),
    path('homewithmyevents/', views.homewithmyevents, name='homewithmyevents'),
    path('login/', views.login, name='login'),
    path('schedule/', views.schedule, name='schedule'),
    path('screening/', views.screening, name='screening'),
    path('signup/', views.signup, name = 'signup'), 
    path('events/', views.events, name = 'events'),  
    path('theatre/', views.theatre, name = 'theatre'),  
     
]
