from tkinter.font import names

from django.urls import path
from .views import index, details, cart, checkout, compare, register, login_user, shop, wishlist, accounts, log_out, get_category_products


urlpatterns = [
    path('', index, name='index'),
    path('details/', details, name='details'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('shop/', shop, name='shop'),
    path('wishlist/', wishlist, name='wishlist'),
    path('compare/', compare, name='compare'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('accounts/', accounts, name='accounts'),
    path('log_out/', log_out, name='log_out'),

    path('category_products/<int:pk>', get_category_products, name='category_products'),
]