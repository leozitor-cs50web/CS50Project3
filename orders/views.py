from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


def signin(request):
    return render(request, "orders/signin.html")


def signup(request):
    return render(request, "orders/signup.html")


def contact(request):
    return render(request, "orders/contact.html")


def about(request):
    return render(request, "orders/about.html")
