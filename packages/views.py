from django.shortcuts import render,redirect
from .models import Packages
from .forms import Packageform
# Create your views here.
def home(request):
    # packages= Package.objects.all()
    # context={
    #     'packages':packages
    # }
    return render(request,'packages/home.html',)

def abtPage(request):
    return render(request,'packages/about.html')


def servicePage(request):
    return render(request,'packages/services.html')

def packages(request):
    package=Packages.objects.all()
    context={'packages':package}
    return render(request,'packages/packages.html',context)
    
def addPackage(request):
    form = Packageform()

    if request.method=='POST':
        form = Packageform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('packages')



    context={'form':form}
    return render(request,'packages/addPackage.html',context)

def updatePackage(request,pk):
    package= Packages.objects.get(id=pk)
    form = Packageform(instance=package)

    if request.method=='POST':
        form = Packageform(request.POST,instance=package)
        if form.is_valid():
            form.save()
            return redirect('packages')



    context={'form':form}
    return render(request,'packages/addPackage.html',context)

def deletePackage(request,pk):
  package= Packages.objects.get(id=pk)
  if request.method=='POST':
    package.delete()
    return redirect('packages')

  context={'package':package}
  return render(request,'packages/deletePackage.html',context)

