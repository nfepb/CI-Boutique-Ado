from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Returns a dictionnary as context processor.
    Makes the dictionnary available to all templates across
    all the application.
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Bag item from the session
    for item_id, item_data in bag.items():
        # Check if item has a size by checking if int
        # If int, we know int data is qty.
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            """
            Adds dictionnary to list of bag items to give access to
            other fields when iterating through itesmmseg. image)
            """
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        # If not int, it is a dictionnary.
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

# Make items available throughout the app
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
