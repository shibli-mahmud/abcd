from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='customer_image', null=True)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    pr_id = models.IntegerField(primary_key=True)
    pr_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.FloatField(max_length=8)
    category = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='product_image', null=True)
    description = models.CharField(max_length=500)


class Order(models.Model):
    o_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    payment_status = models.CharField(max_length=6)


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    method = models.CharField(max_length=10)
    amount = models.FloatField(max_length=8)


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Reviews(models.Model):
    review_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(max_length=3)
    review_details = models.CharField(max_length=500)
    image = models.ImageField(default='default.jpg', upload_to='review_image', null=True)
