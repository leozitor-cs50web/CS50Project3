from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, Topping, UserOrder, Order2, OrderCounter

# need to change depending on the of food addition
menu = ["Regular Pizza", "Sicilian Pizza", "Toppings", "Subs", "Pasta", "Salads", "Dinner Platters"]


# Create your views here.
def index(request):
    print("Usuario Autenticado: {}".format(request.user.is_authenticated))
    # if user is not authenticated
    if not request.user.is_authenticated:
        logged = False
        return render(request, "orders/index.html", {"message": None, "logged": logged})
    # user authenticated
    logged = True
    # select all food available
    regular_pizza = RegularPizza.objects.all()
    sicilian_pizza = SicilianPizza.objects.all()
    topping = Topping.objects.all()
    #need to complete missing food

    context = {
        "user": request.user,
        "logged": logged,
        "menu": menu,
        "regular_pizza": regular_pizza
    }
    return render(request, "orders/index.html", context)


def signin(request):
    # post if comes from sign up page, user created
    if request.method == 'POST':
        username = request.POST["userName"]
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        conf_password = request.POST["confPassword"]
        # verify password and confPassword is equal
        if password != conf_password:
            return render(request, "orders/signup.html",
                          {"message": "Password and Repeat password are different! Try Again!"})
        # check if user exists
        if User.objects.filter(username=username).exists():
            return render(request, "orders/signup.html",
                          {"message": "Username already exist! Try another one!"})
        elif User.objects.filter(email=email).exists():
            return render(request, "orders/signup.html",
                          {"message": "email already registered! Try another one!"})
        else:
            # creating sucessfully user in db
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return render(request, "orders/signin.html", {"message": "userCreated"})
            except:
                return render(request, "orders/signup.html",
                              {"message": "Please! Complete all the fields correctly!"})
    else:
        return render(request, "orders/signin.html")


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/signin.html", {"message": "invalidLogin"})


def logout_view(request):
    logout(request)
    return render(request, "orders/index.html", {"message": "Logged out."})


def signup(request):
    return render(request, "orders/signup.html")


def contact(request):
    return render(request, "orders/contact.html")


def about(request):
    return render(request, "orders/about.html")
