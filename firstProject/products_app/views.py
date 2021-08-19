from django.shortcuts import render, redirect
from .models import OrderList
from django.contrib import messages
from project_app1 import views as projectapp1




def product_list(request):
    products = {
                "dairy": ["milk", "yougurt", "cheese", "butter"],
                "stones": ["rock", "stones", "leva", "molten rock"],
                "tumbleweed": ["weed", "grass", "dead grass"],
                "air": ["smog", "smoke", "atomosphere"]
                }

    return render(request, "products_list.html", products)

def order(request):
    if request.method == "POST":
        prod_list = request.POST.getlist("products")
        prod_str = ",".join(prod_list)
        order_data = OrderList(wholelist=prod_str, username=projectapp1.usrnme)
        order_data.save()
        messages.success(request, "Order created successfully. " + prod_str)
        return redirect("loggedin")

    else:
        return render(request, "products_list.html")