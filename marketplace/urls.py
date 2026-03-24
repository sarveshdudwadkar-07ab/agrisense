from django.urls import path
from .views import product_list, add_to_cart, cart_view, place_order

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('order/', place_order, name='place_order'),
]