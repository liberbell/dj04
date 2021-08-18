from django.shortcuts import render, redirect
from .models import OrderList
from django.contrib import messages



def product_list(request):
    products = {
                "dairy": ["milk", "yougurt", "cheese", "butter"],
                "stones": ["rock", "stones", "leva", "molten rock"],
                "tumbleweed": ["weed", "grass", "dead grass"],
                "air": ["smog", "smoke", "atomosphere"]
                }

    return render(request, "products_list.html", products)