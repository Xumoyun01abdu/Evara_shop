from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def details(request):
    return render(request, 'shop/details.html')

def accounts(request):
    context = {
        "name" : "Account"
    }
    return render(request, 'shop/accounts.html', context)

def cart(request):
    context = {
        "name": "Cart"
    }
    return render(request, 'shop/cart.html', context)

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

def register(request):
    context = {
        "name" : "Register"
    }
    return  render(request, 'shop/login-register.html', context)

def shop(request):
    context = {
        "name" : "Shop"
    }
    return render(request, 'shop/shop.html', context)

def wishlist(request):
    context = {
        "name" : "Wishlist"
    }
    return render(request, 'shop/wishlist.html', context)
