from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    published = models.BooleanField(default=False)
    img = models.ImageField(upload_to='shop/img', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    count = models.IntegerField()
    img = models.ImageField(upload_to='shop/img', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.discount > 0:
            self.discount_price = self.price - self.discount*self.price/100

        super().save(*args, **kwargs)

