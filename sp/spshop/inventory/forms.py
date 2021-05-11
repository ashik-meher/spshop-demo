from django import forms
from django.forms import ModelForm
from .models import Order, Customer, Product, Orderproduct

# user creation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'status', 'note']
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),

            'phone': forms.TextInput(
                attrs= {
                    'class': 'form-control'
                }
            ),

            'email' : forms.TextInput(
                attrs= {
                    'class': 'form-control'

                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'note': forms.TextInput(
                attrs= {
                    'class': 'form-control'
                }
            )

        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class OrderproductForm(forms.ModelForm):

    class Meta:
        model = Orderproduct
        fields = '__all__'



  
  

    #emter wishlist
    """
    create a wishlist
    form
    2 fields
    product dropdown 
    quantity 
    +
    js
    calculate subtotal
    """
    

