from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NST6PDebbZ2nd0792Z7A8H45D8iSHWgUkx7en3eM7GjP2nZzopGXTy7lHIDTUMF3V2P812f3xr5bw326M4QZReL00QfbM0m0f',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)