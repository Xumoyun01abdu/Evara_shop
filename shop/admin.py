from django.contrib import admin
from .models.models import Category, Product
from .models.order import Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
