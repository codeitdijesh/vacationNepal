from django.shortcuts import render,redirect
from .models import Packages,Images,PackageBooking,packagaBookedpeople
from users.models import GuideInfo
from .forms import Packageform
import json
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from smtplib import SMTP
from django.core.mail import get_connection
from django.http import HttpResponse


import smtplib
from django.core.mail import EmailMessage
import smtplib








# Create your views here.
def home(request):
    # packages= Package.objects.all()
    # context={
    #     'packages':packages
    # }
    return render(request,'packages/home.html',)

def abtPage(request):
    return render(request,'packages/about.html')

def singlePackage(request,pk):
    packageObj = Packages.objects.get(id=pk)
    images=Images.objects.filter(packageName=packageObj)
    itenary= packageObj.itenary.split("#")
    context={'package':packageObj,
              'images':images,
              'itenary':itenary}

    return render(request,'packages/singlePackage.html',context)


def servicePage(request):
    return render(request,'packages/services.html')

def packages(request):
    package=Packages.objects.all()
    image=Images.objects.all()
    
    context={'packages':package}
    return render(request,'packages/packages.html',context)

@user_passes_test(lambda u: u.is_superuser)    
def addPackage(request):

    if request.method=='POST':
        # form = Packageform(request.POST)
        itenary=request.POST.getlist('itenary')
        images= request.FILES.getlist('image')
        packageName= request.POST.get('pn')
        defimage= request.FILES.get('defimage')
        location= request.POST.get('location')
        packageDuration= request.POST.get('pd')
        price= request.POST.get('price')
        description= request.POST.get('desc')
        isUnderRated= request.POST.get('isUnderRated')
        if isUnderRated== 'on':
           isUnderRated= True   
        else:
           isUnderRated= False
        
        

        iteListStr=""
        # print(json.dumps(itenary))
        for ite in itenary:
           iteListStr+= ite+"#"

        
        ins= Packages(packageName=packageName,location=location,description=description,defimage=defimage,packageDuration=packageDuration,price=price,isUnderRated= isUnderRated,itenary=iteListStr)
        
        ins.save()

        for image in images:
           Images.objects.create(packageName=ins,image= image)
           
           
    # context={'form':ins}  
    return render(request,'packages/addPackage.html')

@user_passes_test(lambda u: u.is_superuser)
def updatePackage(request,pk):
    package= Packages.objects.get(id=pk)
    form = Packageform(instance=package)
  

    if request.method=='POST':
        
        form = Packageform(request.POST,request.FILES,instance=package)
        if form.is_valid():
            form.save()
            return redirect('packages')

    context={'form':form}
   
    return render(request,'packages/updatePackage.html',context)

@user_passes_test(lambda u: u.is_superuser)
def deletePackage(request,pk):
  package= Packages.objects.get(id=pk)
  if request.method=='POST':
    package.delete()
    return redirect('packages')

  context={'package':package}
  return render(request,'packages/deletePackage.html',context)

def ourGuides(request):
       guides =GuideInfo.objects.all()
       context={'guides':guides}
      
       return render(request,'packages/guides.html',context)

   

def newBooking(request,pk):

 package=Packages.objects.get(id=pk)
 if request.method=='POST':
   peopleNum = request.POST.get('peopleNum')
   peopleNum=int(peopleNum)
   payment=request.POST.get('payment')
   startDate=request.POST.get('date')
   startDate = datetime.strptime(startDate, "%m/%d/%Y")
 
   endDate=startDate+ timedelta(days=package.packageDuration)
   print(startDate,endDate)
   totalprice=int(package.price) *int(peopleNum)
   ins=PackageBooking(packageName=package,packageStartDate=startDate,user=request.user,packageEndDate=endDate,peopleAmt=peopleNum,totalPrice=totalprice)
   ins.save()
   
   context={
    'number':range(1,peopleNum+1),
    'package':package,
    'startDate':startDate,
    'totalprice':totalprice,
    'max_number':int(peopleNum),
     'ins':ins
   }


 return  render(request,'packages/bookingConfirm.html',context)

def newBookingPeople(request,pk):
 

 bookingId= PackageBooking.objects.get(id=pk)
 
 

 if request.method=='POST':
   
   firstName = request.POST.getlist('firstName')
   lastName = request.POST.getlist('lastName')
   age= request.POST.getlist('age')
   gender= request.POST.getlist('gender')
   email= request.POST.getlist('email')
   phone= request.POST.getlist('phone')
 

   for i in range(len(firstName)):
     ins=packagaBookedpeople(PackageBooking = bookingId,firstName=firstName[i],lastName=lastName[i],age=age[i],gender=gender[i],email=email[i],phone=phone[i])
     ins.save()
     print(i)

   price= bookingId.totalPrice/bookingId.peopleAmt 

   context={
      
      'package':bookingId,
      'price':price} 
   
   subject="HEllo"
   
   message="ll "
 
           
   send_email(request)

                      

  
 

 return  render(request,'packages/tourConfirmed.html',context)

@user_passes_test(lambda u: u.is_superuser)
def bookings(request):
   bookings= PackageBooking.objects.all()
   context={'bookings':bookings}

   return render(request,'packages/bookings.html',context)

@user_passes_test(lambda u: u.is_superuser)
def deletebooking(request,pk):
  package= PackageBooking.objects.get(id=pk)

  package.delete()
  return redirect('bookings')

def send_email(request):
   send_mail(
      'subject',
      'her is the message', 
      'vacationnepal640@gmail.com'
      ['di.dk146@gmail.com'],
      fail_silently=False)
   return HttpResponse('Email Sent')

   
       



 

