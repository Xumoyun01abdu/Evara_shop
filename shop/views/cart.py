from django.shortcuts import render, redirect
from ..models.models import Category, Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
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
        

        for pid, number in self.cart.items():
            pd = Product.objects.get(id=pid)
            if pd.discount > 0:
                total = pd.discount_price*number
            else:
                total = pd.price*number

            prd = {
                'number' : number,
                'total' : total,
                'data' : pd
            }

            products.append(prd)

        return products
    
    def clear(self):
        self.cart.clear()
        self.session.modified = True

@csrf_exempt
def add_to_cart(request, product_id):
    cart = Cart(request)
    if Product.objects.filter(id=product_id).exists():
        cart.add(product_id)
        return JsonResponse({"message": "Mahsulot muvaffaqiyatli qo‘shildi", "cart_count" : cart.get_count()} )
    return JsonResponse({"error": "Mahsulot topilmadi"}, status=404)


def get_cart_page(request):
    cart = Cart(request)
    products = cart.get_product()
    cart_total = 0
    subtotal = 0
    profit = 0
    for product in products:
        subtotal += product['total']
        cart_total += product['data'].price * product['number']
        if product['data'].discount_price and product['data'].discount_price > 0:
            profit_price = product['data'].price - product['data'].discount_price
            profit += profit_price * product['number']

    context = {
        "name" : "Cart",
        "cart_count": cart.get_count(),
        "products" : products,
        "cart_total" : cart_total,
        "subtotal" : subtotal,
        "profit" : profit
    }

    return render(request, 'shop/cart.html', context)

