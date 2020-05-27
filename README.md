# Project 3

Web Programming with Python and JavaScript

Video showing the website: https://www.youtube.com/watch?v=7J7tzFkpWI8

This project is a "simulation Fodd delivery" website based on Famous Havard Pizzeria Pinnochio's, made in django.
The layout is build in Bootstrap 4 and some javascript is used to control some menus and functions.

`baseGeneral.html` and `baseGeneral` are the templates that other pages inherits from.

`contact.html`, `about.html` and `contact.html` are pages only for information about the restaurant.

`home.html` is the index page for a nonlogged user, otherwise `homeLogged.html` is the page for when the user logs in
 and displays the menu, shopping cart and other things.
 
 `signin.html` is the page for user login, `signup.html`is the page for user registration.
 
 `shoppingcart.html` is the page where user check all the choices inserted in the cart.
 
 `myOrders.html` is the page for the user check all order he did and also the current status of each one.
 
 `adminOrders.html` and `adminOrder.html` is the page with permission only for staff and website administrator, this 
 way the administrator can check info about all orders and also change and open order to status completed.

main javascript files are `scripts.js` and `scripts.js2` controlling all the button selection and order status behavior

For *Special* pizzas choices i made a random 3 toppings selection, when the user choose it, the server randomize the 3 
topping options that will be used on the pizza.

My personal feature added, is the possibility for the administrator set an order as completed and for the user to check the
current status about his order.