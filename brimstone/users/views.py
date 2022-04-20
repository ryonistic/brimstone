"""Authentication views are listed here, any changes you make will affect
the authentication."""
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login as logthemin, logout as logthemout
from .forms import UserRegisterForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                logthemin(request, user)
                messages.success(request, 'Logged in')
                return redirect('home')
        else:
            return render(request, 'login.html', {})
    else:
        return redirect('home')

def logout(request):
    if request.user.is_authenticated:
        logthemout(request)
        messages.success(request, 'Logged out')
        return redirect('home')
    else:
        messages.success(request, 'You can\'t log out if you are not logged in')
        return redirect('login')

# def register(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = UserRegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password1']
#                 user = authenticate(request, username=username, password=password)
#                 logthemin(request,user)
#                 messages.success(request, 'Registration Successful')
#                 return redirect('home')
#
#         else:
#             form = UserRegisterForm()
#             return render(request, 'register.html', {'form':form})
#     else:
#         messages.success(request, 'You are logged in, log out first.')
#         return redirect('home')

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully, you may now log in!'
    template_name = 'register.html'
