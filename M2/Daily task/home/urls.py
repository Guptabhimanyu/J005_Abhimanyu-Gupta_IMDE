from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('TaskAdd/', views.TaskAdd, name='TaskAdd'),
    path('taskDetails/<str:ag>/', views.taskDetails, name = "detail"),
    path('DailyTask/', views.DailyTask, name="DailyTask"),
    path('taskDelete/<str:id>/', views.taskDelete, name='taskDelete'),
    path('taskUpdate/<str:id>/', views.taskUpdate, name='taskUpdate'),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    
    
]
