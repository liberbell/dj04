from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app_homepage(request):
    return HttpResponse("This is the firstproject App.")