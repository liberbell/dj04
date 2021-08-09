from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def app_homepage(request):
    return render(request, "homepage.html")

def about_us(request):
    return render(request, "aboutus.html")

def services(request):
    return render(request, "services.html")

def contact_us(request):
    return render(request, "contactus.html")