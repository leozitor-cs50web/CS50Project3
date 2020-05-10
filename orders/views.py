from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    print("Usuario Autenticado: {}".format(request.user.is_authenticated))
    if not request.user.is_authenticated:
        logged = False
        return render(request, "orders/index.html", {"message": None, "logged": logged})
    logged = True
    context = {
        "user": request.user,
        "logged": logged
    }
    return render(request, "orders/index.html", context)


def signin(request):
    return render(request, "orders/signin.html")


def signup(request):
    return render(request, "orders/signup.html")


def contact(request):
    return render(request, "orders/contact.html")


def about(request):
    return render(request, "orders/about.html")
