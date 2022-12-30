from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home ,name ='home'),
    path('about',views.abtPage ,name ='about'),
    path('services',views.servicePage ,name ='services'),
    ]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
