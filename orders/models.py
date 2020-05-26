from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class Sub(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, default='initiated')  # initiated - pending - completed
    date = models.DateField(auto_now_add=True)
    totalPriceOrder = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} - date: {self.date} - id: {self.id} - status: {self.status} - total: {self.totalPriceOrder}"


class OrderItem(models.Model):
    number = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    category = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    totalPriceItem = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length=16, default="One Size")
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    topping_allowance = models.IntegerField(default=0)
    topping_1 = models.CharField(max_length=32, default="none")
    topping_2 = models.CharField(max_length=32, default="none")
    topping_3 = models.CharField(max_length=32, default="none")

    def __str__(self):
        return f"{self.name} - ${self.price} Topping_allowance: {self.topping_allowance}"
