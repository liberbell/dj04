from django.shortcuts import render, redirect



def product_list(request):
    products = {
                "dairy": ["milk", "yougurt", "cheese", "butter"],
                "stones": ["rock", "stones", "leva", "molten rock"],
                "tumbleweed": ["weed", "grass", "dead grass"],
                "air": ["smog", "smoke", "atomosphere"]
                }

    return render(request, "products_list.html", products)