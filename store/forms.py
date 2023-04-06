from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from store.models import Product
from store.models import Customer
from store.models import Order
from store.models import Payment
from store.models import Cart
from store.models import Reviews


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'pr_id',
            'pr_name',
            'brand',
            'price',
            'category',
            'image',
            'description'
        ]


class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'c_id',
            'name',
            'image',
            'address',
            'email',
            'phone'
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [

            'customer',
            'product',
            'address',
            'payment_status',
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'payment_id',
            'order',
            'method',
            'amount',
        ]


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'cart_id',
            'customer',
            'product',
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'review_id',
            'product',
            'customer',
            'rating',
            'review_details',
            'image'
        ]


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ]
