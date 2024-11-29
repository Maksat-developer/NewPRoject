from django.contrib import admin

from .models import Product, Customer, Order, OrderItems, ShippingAdress

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ShippingAdress)


