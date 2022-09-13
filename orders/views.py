import imp
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from cart.models import Cart, CartItem
from datetime import datetime
from .models import Order

# Create your views here.
def order(request : HttpRequest):
    cart = Cart.objects.filter(user = request.user, ordered=False)[0]
    cart.ordered = True
    cart.save()
    deliveryDate = request.POST.get('orderDate')
    if deliveryDate == "":
        deliveryDate = datetime.now()
    Order.objects.create(user=request.user, cart = cart, deliveryDate = deliveryDate)
    return redirect("/")