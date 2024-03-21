from django.contrib.auth import logout
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('home',)