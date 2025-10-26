from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .cart import Cart
from ..models.order import Order, OrderItem


class GetCheckoutPageView(LoginRequiredMixin, View):
    def get(self, request):
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
            "name" : "Checkout",
            "cart_count": cart.get_count(),
            "products" : products,
            "cart_total" : cart_total,
            "subtotal" : subtotal,
            "profit" : profit
        }

        return render(request, "shop/checkout.html", context)

    def post(self, request):

        cart = Cart(request)
        user = request.user
        products = cart.get_product()
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        info = request.POST.get('about')

        items = []

        for product in products:
            item, created = OrderItem.objects.get_or_create(
                product = product['data'],
                quantity = product['number'],
                sub_price = product['total']
            )
            items.append(item)

        order = Order(user=user, address = address, phone = phone, info = info)
        order.save()
        order.items.add(*items)
        cart.clear()

        return redirect('index')
    
