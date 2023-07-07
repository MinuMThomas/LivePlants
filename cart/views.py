from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """View cart function"""
   
    return render(request, 'cart/cart.html')
