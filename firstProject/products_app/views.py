from firstProject.firstProject.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from .models import OrderList
from django.contrib import messages
from project_app1 import views as projectapp1
from project_app1 import models as projectmodel
from django.core.mail import send_mail
from django.conf import settings

def product_list(request):
    products = {
                "dairy": ["milk", "yougurt", "cheese", "butter"],
                "stones": ["rock", "stones", "leva", "molten rock"],
                "tumbleweed": ["weed", "grass", "dead grass"],
                "air": ["smog", "smoke", "atomosphere"],
                }

    return render(request, "products_list.html", products)

def order(request):
    if request.method == "POST":
        prod_list = request.POST.getlist("products")
        prod_str = ",".join(prod_list)
        order_data = OrderList(wholelist=prod_str, username=projectapp1.usrnme)
        order_data.save()
        user_data = projectmodel.RegisteredUser.objects.get(name=projectapp1.usrnme)
        receipientlist = [user_data.emailid, ]
        send_mail(
            "Order from Eric Basket",
            "Hi, \n \n Below are the products that you have ordered from Eric Basket.\n\n {}".format(prod_str),
            settings.EMAIL_HOST_USER,
            receipientlist
        )
        messages.success(request, "Order created successfully. " + prod_str)
        return redirect("loggedin")

    else:
        return render(request, "products_list.html")