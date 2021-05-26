

from django.shortcuts import render, redirect
from .models import *

from .forms import *

from .filters import OrderFilter




def land(request):
    return render(request, 'inventory/index.html', {})



def showProducts(request):

    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'inventory/products.html', context)

def addProduct(request):

    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('products')
    
    context = {'form': form}

    
    return render(request, 'inventory/add_product.html', context)


def updateProduct(request, pk):

    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('products')  

    context = {'form': form, 'product': product}

    return render(request, 'inventory/update_product.html', context)


def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {'product': product}

    return render(request, 'inventory/delete_product.html', context)



def show_orders(request):
    orders = Order.objects.all()

    orderproducts = Orderproduct.objects.all()

    #op = orders.orderproduct_set.all()

    orderFilter = OrderFilter(request.GET, queryset=orders)

    orders = orderFilter.qs

    

    context = {'orders': orders, 'orderproducts':orderproducts, 'orderFilter': orderFilter}

    return render(request, "inventory/orders/orders.html", context)



def show_order(request,pk):

    order = Order.objects.get(id=pk)

    items = order.orderproduct_set.all()

    subTotal = 0

    for item in items:
        
        total = item.product.price* item.quantity
        subTotal +=total 

    context = {'order': order, 'items':items, 'subTotal': subTotal}

    return render(request, 'inventory/orders/show_order.html', context)


    #to retrive objects which many to one / foreign key relationships / parent to child

    #first, get the specific object from parent model

    #child_model_objects_associated = parent_object.(child_model_name_in_lowercase)_set.all()




def add_order(request):



    form = OrderForm()
    

    if request.method == 'POST':

        form = OrderForm(request.POST)
        

        if form.is_valid():

            pf = form.save(commit=False)
            pf.save()
               
            return redirect('add-order-product', pk= pf.id)



    context = {'form': form}

    return render(request, 'inventory/orders/add_order.html',  context)




def update_order(request,pk):

    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'inventory/orders/update_order.html', context)



def delete_order(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('show-orders')

    context = {'order': order}

    return render(request, 'inventory/orders/delete_order.html', context)





def add_order_product(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderproductForm()
    

    if request.method == 'POST':

        form = OrderproductForm(request.POST)
        

        if form.is_valid():
            pf = form.save(commit=False)
            pf.order = order
            pf.save()

            return redirect('add-order-product', pk=order.id)
            #return redirect('show-orders')

    context = {'form': form, 'order': order}
    
    return render(request,'inventory/ordered_products/add_order_product.html', context)

def test_order(request):

    return render(request, 'inventory/ordered_products/test_order.html')