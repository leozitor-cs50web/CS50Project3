from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from django.contrib.auth.models import User

from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, Topping, UserOrder, OrderItem


def context_send(request):
    """ simplify the context dictionary containing info for each request"""
    userOrder = UserOrder.objects.get(user=request.user, status='initiated')
    allUserOrders = UserOrder.objects.filter(user=request.user)
    orderItems = OrderItem.objects.filter(number=userOrder)
    itemsCount = orderItems.count()
    # select all food available
    regular_pizza = RegularPizza.objects.all()
    sicilian_pizza = SicilianPizza.objects.all()
    sub = Sub.objects.all()
    pasta = Pasta.objects.all()
    salad = Salad.objects.all()
    dinner_platter = DinnerPlatter.objects.all()
    topping = Topping.objects.all()
    #  check if the button of admin appears or not
    if request.user.is_staff:
        staff = True
    else:
        staff = False
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
        "itemsCount": itemsCount,
        "allUserOrders": allUserOrders,
        "order": userOrder,
        "staff": staff
    }
    return context


def context_send_admin(request):
    """ simplify the context dictionary containing info for each request"""
    itemsCount = OrderItem.objects.filter(number=UserOrder.objects.get(user=request.user, status='initiated')).count()
    # select all food available
    regular_pizza = RegularPizza.objects.all()
    sicilian_pizza = SicilianPizza.objects.all()
    sub = Sub.objects.all()
    pasta = Pasta.objects.all()
    salad = Salad.objects.all()
    dinner_platter = DinnerPlatter.objects.all()
    topping = Topping.objects.all()
    #  check if the button of admin appears or not
    if request.user.is_staff:
        staff = True
    else:
        staff = False
    context = {
        "user": request.user,
        "regular_pizza": regular_pizza,
        "sicilian_pizza": sicilian_pizza,
        "sub": sub,
        "pasta": pasta,
        "salad": salad,
        "dinner_platter": dinner_platter,
        "toppings": topping,
        "itemsCount": itemsCount,
        "staff": staff
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
                user_order = UserOrder.objects.create(user=user)
                user_order.save()
                return render(request, "orders/signin.html", {"message": "userCreated"})
            except:
                return render(request, "orders/signup.html",
                              {"message": "Please! Complete all the fields correctly!"})
    else:
        if not request.user.is_authenticated:
            return render(request, "orders/signin.html")
        else:
            context = context_send(request)
            return render(request, "orders/homeLogged.html", context)


def signup(request):
    if not request.user.is_authenticated:
        return render(request, "orders/signup.html")
    else:
        context = context_send(request)
        return render(request, "orders/homeLogged.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/signin.html", {"message": "invalidLogin"})
    else:
        return render(request, "orders/signin.html")


def logout_view(request):
    logout(request)
    return render(request, "orders/home.html", {"message": "Logged out."})


@login_required(login_url='login')
def add_item(request, category, name, price, size):
    try:
        userOrder = UserOrder.objects.get(user=request.user, status='initiated')
        if OrderItem.objects.filter(number=userOrder, category=category, name=name, price=price).exists():
            item = OrderItem.objects.get(number=userOrder, category=category, name=name, price=price)
            item.quantity = int(item.quantity) + 1
            item.totalPriceItem = float(item.quantity) * float(item.price)
            userOrder.totalPriceOrder = float(userOrder.totalPriceOrder) + float(item.price)
        else:
            item = OrderItem(number=userOrder, category=category, name=name, price=price, totalPriceItem=price)
            userOrder.totalPriceOrder = float(userOrder.totalPriceOrder) + float(item.price)
        if category == 'Regular Pizza' or category == 'Sicilian Pizza':
            if name == '1 topping':
                item.topping_allowance = 1
            if name == '2 toppings':
                item.topping_allowance = 2
            if name == '3 toppings':
                item.topping_allowance = 3
        if category != 'Pasta' or category != 'Salad':
            item.size = size
        item.save()
        userOrder.save()
        context = context_send(request)
        return render(request, "orders/homeLogged.html", context)
    except:
        context = context_send(request)
        return render(request, "orders/homeLogged.html", context)


@login_required(login_url='login')
def add_topping(request):
    try:
        item_id = int(request.POST["itemId"])
        item = OrderItem.objects.get(id=item_id)
        # querying toppings
        top1 = request.POST["top1"]
        item.topping_1 = top1
        # print(type(top1))
        if item.topping_allowance > 1:
            top2 = request.POST["top2"]
            item.topping_2 = top2
        # print(top2)
        if item.topping_allowance > 2:
            top3 = request.POST["top3"]
            item.topping_3 = top3
        #   print(top3)
        # print(item_id)
        # print(item.topping_3)
        item.topping_allowance = -1
        item.save()
        context = context_send(request)
        return render(request, "orders/shoppingcart.html", context)
    except:
        context = context_send(request)
        return render(request, "orders/shoppingcart.html", context)


@login_required(login_url='login')
def remove_item(request, item_id, option):
    try:
        item = OrderItem.objects.get(id=item_id)
        userOrder = UserOrder.objects.get(user=request.user, status='initiated')
        userOrder.totalPriceOrder = float(userOrder.totalPriceOrder) - float(item.totalPriceItem)
        userOrder.save()
        item.delete()
    except:
        context = context_send(request)
        return render(request, "orders/homeLogged.html", context)

    context = context_send(request)
    if option == 'cart':
        return render(request, "orders/shoppingcart.html", context)
    elif option == 'home':
        return render(request, "orders/homeLogged.html", context)
    elif option == 'checkout':
        return render(request, "orders/checkout.html", context)


@login_required(login_url='login')
def shoppingcart(request):
    context = context_send(request)
    return render(request, "orders/shoppingcart.html", context)


@login_required(login_url='login')
def sucess(request):
    user = request.user
    order = UserOrder.objects.get(user=user, status='initiated')
    # changes the order object parameter and creates a new one to the user
    order.status = 'pending'  # changing to pending
    order.save()
    order = UserOrder.objects.create(user=user)
    order.save()
    context = context_send(request)
    return render(request, "orders/sucessOrder.html", context)


@login_required(login_url='login')
def orders(request, order_page):
    context = context_send(request)
    user_orders = context["allUserOrders"]
    user_orders_count = user_orders.count()
    context["allUserOrdersCount"] = user_orders_count
    orderPageList = []
    if user_orders_count < 11:
        return render(request, "orders/myOrders.html", context)
    else:
        allUserOrders = UserOrder.objects.filter(user=request.user)
        for i in range(0, user_orders_count - 10, 10):
            orderPageList.append(allUserOrders[user_orders_count - i - 10:user_orders_count - i])
        orderPageList.append(allUserOrders[0:user_orders_count % 10])
        context["allUserOrder"] = orderPageList[order_page - 1]
        context["allUserOrders"] = orderPageList
        return render(request, "orders/myOrders.html", context)


@staff_member_required
def adminorders(request, order_type, order_page):
    context = context_send_admin(request)
    if order_type == 'initiated':
        all_orders = UserOrder.objects.filter(status='initiated')
        context["orderType"] = 'initiated'
    elif order_type == 'pending':
        all_orders = UserOrder.objects.filter(status='pending')
        context["orderType"] = 'pending'
    elif order_type == 'completed':
        all_orders = UserOrder.objects.filter(status='completed')
        context["orderType"] = 'completed'
    else:
        all_orders = UserOrder.objects.all()
        context["orderType"] = 'all'
    all_orders_count = all_orders.count()
    context["allOrdersCount"] = all_orders_count
    if all_orders_count < 11:
        context["allUserOrder"] = all_orders
        return render(request, "orders/adminOrders.html", context)
    else:
        orderPageList = []
        for i in range(0, all_orders_count - 10, 10):
            orderPageList.append(all_orders[all_orders_count - i - 10:all_orders_count - i])
        orderPageList.append(all_orders[0:all_orders_count % 10])
        context["allUserOrder"] = orderPageList[order_page - 1]
        context["allUserOrders"] = orderPageList
        return render(request, "orders/adminOrders.html", context)


@staff_member_required
def changeorders(request, order_id):
    order = UserOrder.objects.get(id=order_id)
    context = context_send_admin(request)
    context["items"] = OrderItem.objects.filter(number=order)
    context["order"] = order
    if request.method == 'POST':
        if UserOrder.objects.filter(id=order_id, status="pending").exists():
            order.status = "completed"
            order.save()
            return render(request, "orders/adminOrder.html", context)
        else:
            return render(request, "orders/adminOrder.html", context)
    else:
        return render(request, "orders/adminOrder.html", context)


@login_required(login_url='login')
def checkout(request):
    user = request.user
    order = UserOrder.objects.get(user=user, status='initiated')
    context = context_send(request)
    # checking if the cart has at least 1 item
    if OrderItem.objects.filter(number=order).exists():
        return render(request, "orders/checkout.html", context)
    else:
        context["message"] = "You Should add at least one item, before checking out"
        return render(request, "orders/homeLogged.html", context)


def contact(request):
    return render(request, "orders/contact.html")


def about(request):
    return render(request, "orders/about.html")
