from django.shortcuts import render, redirect
from django.http import request


def product_list(reuqest):
    products = {
                "dairy": ["milk", "yougurt", "cheese", "butter"]
                # "stones": ["rock", "stones", "leva", "molten rock"],
                # "tumbleweed": ["weed", "grass", "dead grass"],
                # "air": ["smog", "smoke", "atomosphere"]
                }

    return render(request, "products_list.html", products)