from django.shortcuts import render,redirect
from .models import Packages,Images
from .forms import Packageform
import json
from django.contrib.auth.decorators import user_passes_test

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
    print(itenary)
    print(packageObj)
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

        print(iteListStr)   
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

