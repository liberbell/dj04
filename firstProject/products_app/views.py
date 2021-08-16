from django.shortcuts import render, redirect

# Create your views here.

def product_list(reuqest):
    products = {"diary": ["milk", "yougurt", "cheese", "butter"],
                "stones": ["rock", "stones", "leva", "molten rock"],
                }