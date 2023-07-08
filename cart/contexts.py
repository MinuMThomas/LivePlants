from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery': free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
