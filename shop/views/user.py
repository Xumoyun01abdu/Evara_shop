from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ..forms import LoginForm, RegisterForm



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
            user.set_password(password)
            user.save()
            return redirect('register')

    form = RegisterForm()
    context = {
        "name" : "Register",
        "form" : form
    }
    return  render(request, 'shop/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

    form = LoginForm()
    context = {
        "name": "Login",
        "form" : form
    }
    return render(request, 'shop/login.html', context)

def log_out(request):
    logout(request)
    return redirect('index')


def accounts(request):
    context = {
        "name" : "Account"
    }
    return render(request, 'shop/accounts.html', context)