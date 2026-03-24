from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'marketplace/products.html', {'products': products})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'marketplace/cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    if cart_items.exists():
        Order.objects.create(user=request.user, total_amount=total)
        cart_items.delete()

    return redirect('product_list')