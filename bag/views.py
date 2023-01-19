from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    View to render the bag contents page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified products to the shopping bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # If there is a bag variable in the session, adds to dictionnary,
    # if not, creates one
    bag = request.session.get('bag', {})

    if size:
        # if item is already in bag:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'Updated size {size.upper()} {product.name} \
                        quantity to {bag[item_id]["items_by_size"][size]}'
                    )

            else:
                # If item already in bag but not in size:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} {product.name} \
                        to your bag'
                    )
        # If not already in bag, will add item and list by size of items.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f"Added {size.upper()} {product.name} to your bag"
                )

    else:
        if item_id in list(bag.keys()):
            # Updates the quantity if already in bag
            bag[item_id] += quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
                )

        else:
            # Adds item to the bag if not in bag
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag")

# Overwrites the variable in the session with updated version
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjusts the quantity of the specified products to the shopping bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # If there is a bag variable in the session, adds to dictionnary,
    # if not, creates one
    bag = request.session.get('bag', {})

    if size:
        # if item is already in bag:
        if quantity > 0:
            """
            Drill items by size dictionnary,
            find specific size, update qty
            """
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                    request, f"Updated {size.upper()} {product.name} \
                        to your {bag[item_id]['items_by_size'][size]}"
                    )

        else:
            # Remove item if qty = 0
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f"Removed {size.upper()} {product.name} \
                        from your bag"
                    )
    else:
        if quantity > 0:
            """
            If qty is 0, removes the item
            """
            bag[item_id] = quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
                )
        else:
            # Remove item if qty = 0
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")


# Overwrites the variable in the session with updated version
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag.
    No qty needed as intended qty is 0.
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        """
        If size is in POST, we want to remove item size key
        in items by size dictionnary.
        """
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f"Removed {size.upper()} {product.name} \
                        from your bag"
                    )
        else:
            """If the qty is already 0, remove the item_id"""
            bag.pop(item_id)
            messages.success(request, f"Removed {product.name} from your bag")

        request.session['bag'] = bag
        """
        200 http return because view posted from JS function.
        """
        return HttpResponse(status=200)

    except Exception as e:
        """Return 500 error in case anything goes wrong."""
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
