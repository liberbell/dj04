from django.db import models
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse, request
from .models import RegisteredUser
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.

def app_homepage(request):
    try:
        if usrnme:
            userdetails = {"username": usrnme}
            return render(request, "loggedin.html", userdetails)
    except NameError:
        return render(request, "homepage.html")

def about_us(request):
    try:
        if usrnme:
            return render(request, "aboutus.html")
    except NameError:
        return render(request, "aboutus.html")

def services(request):
    try:
        if usrnme:
            return render(request, "services.html")
    except NameError:
        return render(request, "services.html")

def contact_us(request):
    try:
        if usrnme:
            return render(request, "contactus.html")
    except NameError:
        return render(request, "contactus.html")

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("signin")
        
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)

def signin(request):
    global usrnme
    if request.method == "POST":
        usrnme = request.POST["username"]
        psswrd = request.POST["pswd"]

        try:
            user = RegisteredUser.objects.get(name=usrnme)
            print(user.name)
            print(user.password)
            if usrnme == user.name and psswrd == user.password:
                return redirect("loggedin")
            
            else:
                messages.info(request, "Incollect password.")
                return redirect("signin")

        except ObjectDoesNotExist:
            messages.info(request, "The user does not exist.")
            return redirect("signin")

    else:
        return render(request, "signin.html")

def loggedin(request):
    userdetails = {"username": usrnme}
    return render(request, "loggedin.html", userdetails)

def logout(request):
    global usrnme
    del usrnme
    return render(request, "logout.html")

class UserListView(ListView):
    model = RegisteredUser
    template_name = "user_data.html"
    context_object_name = "alldata"

class UserDetailView(DetailView):
    model = RegisteredUser

class UserCreateView(CreateView):
    model = RegisteredUser
    form_class = RegisterForm