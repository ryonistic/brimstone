from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as logthemin, logout as logthemout


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
