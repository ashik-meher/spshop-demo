from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('', views.land, name="dashboard"),
   path('products', views.showProducts, name="products"),
   path('add-product', views.addProduct, name="add-product"),
   path('update-product/<str:pk>', views.updateProduct, name="update-product"),
   path('delete-product/<str:pk>', views.deleteProduct, name="delete-product"),
   path('orders', views.show_orders, name="show-orders"),
   path('add-order', views.add_order, name="add-order"),
   path('orders/<str:pk>', views.show_order, name="show-order"),
   path('update-order/<str:pk>', views.update_order, name="update-order"),
   path('delete-order/<str:pk>', views.delete_order, name="delete-order"),
   path('add-order-product', views.add_order_product, name="add-order-product"),
   path('test-order', views.test_order, name="test-order")





]
