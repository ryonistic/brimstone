from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as logthemin, logout as logthemout
from .forms import UserRegisterForm
from django.contrib import messages


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                logthemin(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html', {})
    else:
        return redirect('home')

def logout(request):
    if request.user.is_authenticated:
        logthemout(request)
        return redirect('home')
    else:
        return redirect('login')

def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                logthemin(request,user)
                messages.success(request, 'Registration Successful')
                return redirect('home')
            else:
                messages.success(request, 'There was an error with your details.')
                return redirect('register')
        else:
            form = UserRegisterForm()
            return render(request, 'register.html', {'form':form})
    else:
        return redirect('home')

