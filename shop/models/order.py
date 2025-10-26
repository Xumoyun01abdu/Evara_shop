from django.db import models
from django.contrib.auth.models import User
from .models import Product

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sub_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Order item {self.product.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField('OrderItem')
    address = models.CharField(max_length=300, null=True, blank=True)
    phone = models.IntegerField()
    info = models.TextField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s order"
    