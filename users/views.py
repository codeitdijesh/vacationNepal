from django.shortcuts import render
from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from .forms import CustomUserCreationForm,Guideform
from django.views.decorators.csrf import csrf_exempt
# from .models import GuideInfo


# Create your views here.
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request,'users/login.html')
  


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
  
    return redirect('log')
@csrf_exempt
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.first_name=form.cleaned_data.get('first_name')
            user.last_name=form.cleaned_data.get('last_name')
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('home')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request,'users/login.html',context)

@login_required(login_url='log')
def applyGuide(request):
 form = Guideform()
 if request.method=='POST':
    form = Guideform(request.POST, request.FILES)
    if form.is_valid():
    
        form.save()
        messages.success(request, 'Your request has been send to admin')

        return redirect('home')
 context= {
    'form': form
 }
 
 return render(request,'users/applyGuide.html',context)

def addNotification(newGuide):
     print(newGuide.name)


     