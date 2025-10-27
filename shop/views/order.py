from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from asgiref.sync import async_to_sync
from .cart import Cart
from ..models.order import Order, OrderItem
from .telegram import send_message


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

        order_text = self.get_order_text(user=user, address=address, phone=phone, items=items, info=info, order=order)

        async_to_sync(send_message)(order_text)

        return redirect('index')
    
    def get_order_text(self, user, address, phone, items, info, order):
        order_text = f"Yangi buyurtma\n\n"
        order_text += f"<b>Foydalanuvchi:</b> {user.username}\n"
        order_text += f"<b>Email:</b> {user.email if user.email else "Mavjud emas"}\n"
        order_text += f"<b>Manzil:</b> {address}\n"
        order_text += f"<b>Qo'shimcha ma'lumot:</b> {info}\n"
        order_text += f"<b>Telefon:</b> {phone}\n"
        order_text += f"<b>Sana:</b> {order.created_at.strftime('%Y:%m:%d %H:%M')}\n"
        order_text += f"<b>Holat:</b> {order.status}\n"
        order_text += f"<b>Buyurtma tarkibi:</b> \n"

        total_sum = 0
        for item in items:
            p = item.product
            line = f"- {p.name} | Soni: {item.quantity} | Narxi: {item.sub_price}$ \n"
            order_text += line
            total_sum += item.sub_price
        
        order_text += f"Buyurtma umumiy summasi: {total_sum}$"

        return order_text