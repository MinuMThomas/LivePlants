from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from items.models import Item


def view_cart(request):
    """ A view to return the shopping-cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified item to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    item = get_object_or_404(Item, pk=item_id)

    try:
        if item_id in list(cart.keys()):
            if cart[item_id] + quantity > 99:
                cart[item_id] = 99
                messages.success(request, f'{item} successfully added to Cart!')
            else:
                cart[item_id] += quantity
                
        else:
            cart[item_id] = quantity
            messages.success(request, f'{item} successfully added to Cart!')
    except RuntimeError:
        messages.error(request, "Whoops, We've encountered a problem, we'll get straight onto it, in the meantime you could always try again??")

    request.session['cart'] = cart
    return redirect(redirect_url)