from django.contrib import admin
from inventory.models import Product, OrderDetail, Order, Customer, WireSize


# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Customer)
admin.site.register(WireSize)
