from django.contrib import admin
from .models.models import Category, Product

admin.site.register([Category, Product])
