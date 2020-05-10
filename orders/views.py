from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User


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


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/signin.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "Logged out."})


def signup(request):
    return render(request, "orders/signup.html")


def createUser(request):
    userName = request.POST["userName"]
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    email = request.POST["email"]
    password = request.POST["password"]
    confPassword = request.POST["confPassword"]
    user = User.objects.create_user(userName, email, password)



def contact(request):
    return render(request, "orders/contact.html")


def about(request):
    return render(request, "orders/about.html")
