

from django.urls import path
from shop.views.user import  register, login_user, accounts, log_out
from shop.views.shop import index, details, compare, shop, wishlist, get_category_products
from shop.views.order import GetCheckoutPageView
from shop.views.cart import add_to_cart, get_cart_page


urlpatterns = [
    path('', index, name='index'),
    path('details/', details, name='details'),

    path('checkout/', GetCheckoutPageView.as_view(), name='checkout'),

    path('shop/', shop, name='shop'),
    path('wishlist/', wishlist, name='wishlist'),
    path('compare/', compare, name='compare'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('accounts/', accounts, name='accounts'),
    path('log_out/', log_out, name='log_out'),

    path('category_products/<int:pk>', get_category_products, name='category_products'),

    path('cart/add/<int:product_id>/', add_to_cart),
    path('get_cart/', get_cart_page, name='get_cart')
]