from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "orders/signin.html")


def signin(request):
    return render(request, "orders/signin.html")
