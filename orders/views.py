from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from django.contrib.auth.models import User

from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, Topping, UserOrder, OrderItem


def context_send(request):
    """ simplify the context dictionary containing info for each request"""
    userOrder = UserOrder.objects.get(user=request.user, status='initiated').order_number
    orderItems = OrderItem.objects.filter(number=userOrder)
    print(orderItems)
    if orderItems.count() == 0:
        total = 0.00
    else:
        total = list(orderItems.aggregate(Sum('price')).values())[0]
        total = float(total)
    itemsCount = orderItems.count()
    total = "{:.2f}".format(total)
    # select all food available
    regular_pizza = RegularPizza.objects.all()
    sicilian_pizza = SicilianPizza.objects.all()
    sub = Sub.objects.all()
    pasta = Pasta.objects.all()
    salad = Salad.objects.all()
    dinner_platter = DinnerPlatter.objects.all()
    topping = Topping.objects.all()

    context = {
        "user": request.user,
        "regular_pizza": regular_pizza,
        "sicilian_pizza": sicilian_pizza,
        "sub": sub,
        "pasta": pasta,
        "salad": salad,
        "dinner_platter": dinner_platter,
        "toppings": topping,
        "items": orderItems,
        "total": total,
        "itemsCount": itemsCount,
    }
    return context


# Create your views here.
def index(request):
    # print("Usuario Autenticado: {}".format(request.user.is_authenticated))
    # if user is not authenticated
    if not request.user.is_authenticated:
        return render(request, "orders/home.html", {"message": None})

    # user authenticated
    context = context_send(request)

    return render(request, "orders/homeLogged.html", context)


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
            # creating sucessfully user in db and also a order pointing it
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                order_number = UserOrder(user=user)
                order_number.order_number = order_number.id
                order_number.save()
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
    return render(request, "orders/home.html", {"message": "Logged out."})


def add_item(request, category, name, price, size):
    item = OrderItem(number=request.user.id, category=category, name=name, price=price)
    if category == 'Regular Pizza' or category == 'Sicilian Pizza':
        if name == '1 topping':
            item.topping_allowance = 1
        if name == '2 toppings':
            item.topping_allowance = 2
        if name == '3 toppings':
            item.topping_allowance = 3
    if category != 'Pasta' or category != 'Salads':
        item.size = size
    item.save()
    context = context_send(request)

    return render(request, "orders/homeLogged.html", context)


def remove_item(request, item_id, option):
    item = OrderItem.objects.get(id=item_id)
    item.delete()
    # user authenticated
    context = context_send(request)

    if option == 'cart':
        return render(request, "orders/shoppingcart.html", context)
    elif option == 'home':
        return render(request, "orders/homeLogged.html", context)
    elif option == 'checkout':
        return render(request, "orders/checkout.html", context)


def shoppingcart(request):
    context = context_send(request)
    return render(request, "orders/shoppingcart.html", context)


def checkout(request):
    context = context_send(request)
    return render(request, "orders/checkout.html", context)


def signup(request):
    return render(request, "orders/signup.html")


def contact(request):
    return render(request, "orders/contact.html")


def about(request):
    return render(request, "orders/about.html")
