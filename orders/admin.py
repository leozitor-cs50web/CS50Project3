from django.contrib import admin

from .models import RegularPizza, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter, Topping, UserOrder, Order2, OrderCounter

# Register your models here.
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Topping)
admin.site.register(UserOrder)
admin.site.register(Order2)
admin.site.register(OrderCounter)

