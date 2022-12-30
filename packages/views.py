from django.shortcuts import render
from .models import Package

# Create your views here.
def home(request):
    packages= Package.objects.all()
    context={
        'packages':packages
    }
    return render(request,'packages/home.html',context)

def abtPage(request):
    return render(request,'packages/about.html')


def servicePage(request):
    return render(request,'packages/services.html')