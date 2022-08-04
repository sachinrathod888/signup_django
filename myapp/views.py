from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def registerpage(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request,'user account has been successfully created for' + user)
            return redirect('signin')

    return render(request,'myapp/signup.html',{'form':form})

def loginpage(request):
    username = request.POST.get('username')
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        messages.info(request,'Username or Password is incorrect')

    
    return render(request,'myapp/signin.html')

def logoutpage(request):
    pass