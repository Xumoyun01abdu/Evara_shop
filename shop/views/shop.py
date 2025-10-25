from django.shortcuts import render, redirect
from ..models.models import Category, Product
from .cart import Cart


def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    cart = Cart(request)

    context = {
        'categories': category,
        'products': products,
        'cart_count' : cart.get_count()
    }
    return render(request, 'shop/index.html', context)

def details(request):
    return render(request, 'shop/details.html')



def checkout(request):
    cart = Cart(request)
    context = {
        "name" : "Checkout",
        'cart_count' : cart.get_count()
    }
    return render(request, 'shop/checkout.html', context)

def compare(request):
    cart = Cart(request)
    context = {
        "name" : "Compare",
        'cart_count' : cart.get_count()
    }
    return render(request, 'shop/compare.html', context)


def shop(request):
    products = Product.objects.all()
    cart = Cart(request)

    context = {
        "name" : "Shop",
        "products" : products,
        'cart_count' : cart.get_count()
    }
    return render(request, 'shop/shop.html', context)

def wishlist(request):
    cart = Cart(request)
    context = {
        "name" : "Wishlist",
        'cart_count' : cart.get_count()
    }
    return render(request, 'shop/wishlist.html', context)


def get_category_products(request, pk):
    cart = Cart(request)
    products = Product.objects.filter(category_id=pk)
    context = {
        "products" : products,
        "name" : "Category",
        'cart_count' : cart.get_count()
    }

    return render(request, 'shop/category_product.html', context)