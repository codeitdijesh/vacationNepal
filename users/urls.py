from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings



urlpatterns = [
    path('login/',views.loginUser,name='log'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logO'),
    path('applyGuide/',views.applyGuide,name='applyGuide'),
    path('notifications/',views.notifications,name='notifications'),
    path('delete-notification<str:pk>/',views.deleteNotification,name='delete-noti'),
    path('approve-notification<str:pk>/',views.approveNotification,name='approve-noti'),
    path('guideAccount<str:pk>/',views.guideAcc,name='guideAcc')
    ]

