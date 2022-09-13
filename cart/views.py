import imp
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Cart, CartItem
from products.models import Product
from datetime import datetime

# Create your views here.
def add(request : HttpRequest):
    # print("###### Debug #############")
    cart = Cart.objects.filter(user = request.user, ordered=False)
    count = request.GET.get('count')
    prod = request.GET.get('id')
    # print(prod, count)
    product = Product.objects.filter(pk = prod)
    if len(product) == 0:
        product = None
    else:
        product = product[0]
    if product is None:
        return redirect("/products")
    if count == "":
        count = 1
    if len(cart) == 0:
        cart = Cart.objects.create(user=request.user, price= product.price * int(count))  
        item = CartItem.objects.create(product=product, quantity = int(count), price = product.price * int(count), cart = cart)
    else:
        cart = cart[0]
        cart.price = cart.price + product.price * int(count)
        cart.save()
        prod_exist = CartItem.objects.filter(cart=cart, product=product)
        if len(prod_exist) > 0:
            prod_exist = prod_exist[0]
            prod_exist.quantity = prod_exist.quantity + int(count)
            prod_exist.price = prod_exist.price + int(count) * product.price 
            prod_exist.save()
        else:
            item = CartItem.objects.create(product=product, quantity = int(count), price = product.price * int(count), cart = cart)
    return redirect('/products')
        

def view(request : HttpRequest):
    cart = Cart.objects.filter(user = request.user, ordered=False)
    if len(cart) > 0:
        cart = cart[0]
    else:
        return redirect('/products')
    items = CartItem.objects.filter(cart = cart)
    return render(request, 'cart.html', {'items' : items, 'total': cart.price})

def remove(request : HttpRequest):
    prodId = request.GET.get('id')
    item = CartItem.objects.get(id=prodId)
    item.cart.price = item.cart.price - item.price
    item.cart.save()
    item.delete()
    return redirect("/cart/view")
    