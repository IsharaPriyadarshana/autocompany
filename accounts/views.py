import imp
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request : HttpRequest):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "username taken!")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered!")
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name = first_name, last_name=last_name)
                user.save()
                messages.info(request,"user Created!")
                return redirect('login')
            return redirect("register")
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")
    else:
        return render(request, 'register.html')


def login(request : HttpRequest):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            next = '/'
            if request.POST.get('next') != '':
                next = request.POST.get('next')
            return redirect(next)
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
