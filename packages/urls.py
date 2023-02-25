from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home ,name ='home'),
    path('addPackage',views.addPackage,name ='addPackage'),
    path('updatePackage/<str:pk>/',views.updatePackage,name ='updatePackage'),
    path('deletePackage/<str:pk>/',views.deletePackage,name ='deletePackage'),
    path('deletebooking/<str:pk>/',views.deletebooking,name ='deletebooking'),
    path('packages',views.packages,name ='packages'),
    path('singlePackage/<str:pk>/',views.singlePackage,name ='singlePackage'),
    path('guides/',views.ourGuides,name ='guides'),
    path('about',views.abtPage ,name ='about'),
    path('bookings',views.bookings ,name ='bookings'),
    path('services',views.servicePage ,name ='services'),
    path('newBooking/<str:pk>/',views.newBooking ,name ='newBooking'),
    path('newBookingPeople/<str:pk>/',views.newBookingPeople,name ='newBookingPeople'),
    ]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
