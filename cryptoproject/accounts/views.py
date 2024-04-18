from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import *

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')


def signup_form(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully created. Please log in.')  # Add a success message
            return redirect('accounts:login-page')
    else:
        form = SignupForm()
        
        
    context = {"form":form}   
    return render(request, 'accounts/signup.html', context)


def login_form(request):
    
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                return redirect('accounts:dashboard')
            
    context = {"form":form}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='accounts:login-page')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect("/")