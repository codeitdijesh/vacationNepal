from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    path('login/',views.loginUser,name='log'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logO'),
    path('applyGuide/',views.applyGuide,name='applyGuide'),
    ]

