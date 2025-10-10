from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Category, Product

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
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password']
        email = request.POST['email']
        if username and password and password2 and password:
            if password == password2:
                user = User(username=username, password=password, email=email)
                user.set_password(password)
                user.save()
                return redirect('register')
    context = {
        "name" : "Register"
    }
    return  render(request, 'shop/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    context = {
        "name": "Login"
    }
    return render(request, 'shop/login.html', context)


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


def log_out(request):
    logout(request)
    return redirect('index')

def get_category_products(request, pk):
    products = Product.objects.filter(category_id=pk)
    context = {
        "products" : products,
        "name" : "Category"
    }

    return render(request, 'shop/category_product.html', context)