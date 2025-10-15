from django.shortcuts import render, redirect
from ..models.models import Category, Product

def index(request):
    category = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': category,
        'products': products,
    }
    return render(request, 'shop/index.html', context)

def details(request):
    return render(request, 'shop/details.html')



def checkout(request):
    context = {
        "name" : "Checkout"
    }
    return render(request, 'shop/checkout.html', context)

def compare(request):
    context = {
        "name" : "Compare"
    }
    return render(request, 'shop/compare.html', context)


def shop(request):
    products = Product.objects.all()

    context = {
        "name" : "Shop",
        "products" : products,
    }
    return render(request, 'shop/shop.html', context)

def wishlist(request):
    context = {
        "name" : "Wishlist"
    }
    return render(request, 'shop/wishlist.html', context)


def get_category_products(request, pk):
    products = Product.objects.filter(category_id=pk)
    context = {
        "products" : products,
        "name" : "Category"
    }

    return render(request, 'shop/category_product.html', context)