from django.shortcuts import render, redirect
from ..models.models import Category, Product
from django.http import JsonResponse

class Cart:
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')

        if not cart:
            cart = self.session['session_key']={}
        
        self.cart = cart

    def add(self, product_id):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1

        self.session.modified = True

    def get_count(self):
        return len(self.cart.keys())
    
    def get_product(self):
        products = []

        for pid in self.cart.keys():
            products.append(Product.objects.get(id=pid))

        return products

def add_to_cart(request, product_id):
    cart = Cart(request)
    if Product.objects.filter(id=product_id):
        cart.add(product_id)
    
    return JsonResponse({"message": "Muvaffaqqiyatli"})

def get_cart_page(request):
    cart = Cart(request)
    products = cart.get_product()
    print(products)
    context = {
        "name" : "Cart",
        "cart_count": cart.get_count(),
        "products" : products
    }
    return render(request, 'shop/curt.html', context)

    