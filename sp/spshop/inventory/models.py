

from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        ('Food and Bevarage', 'Food and Bevarage'),
        
    )

    code = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    price = models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    Tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (

        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),

    )

    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='not set')
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

  
  

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
    


    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        orderDate = str(self.date_created) 
        return ('ORDER-'+ str(self.id) + '-'+self.name + '-' + orderDate[0:10])
    



class Orderproduct(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    quantity = models.IntegerField()
    
  




"""
https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
"""