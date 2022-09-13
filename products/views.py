import imp
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Product
from cart.models import Cart, CartItem

# Create your views here.

def products(request : HttpRequest):
    if not request.user.is_authenticated:
        return redirect('/accounts/login?next=/products/')
    else:
        products = Product.objects.all()
        item_count = 0
        cart = Cart.objects.filter(user=request.user, ordered=False)
        if len(cart) > 0:
            item_count = len(CartItem.objects.filter(cart=cart[0]))

        return render(request, 'products.html', {'products' : products , 'itemCount' : item_count})

def detail(request : HttpRequest):
    prod = request.GET.get('product')
    products = Product.objects.filter(name=prod)
    if len(products) != 1:
        return redirect("/products")
    else:
        return render(request, 'product.html', {'product' : products[0]})
