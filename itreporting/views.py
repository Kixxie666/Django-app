from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'profile'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'})

