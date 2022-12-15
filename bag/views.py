from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """
    View to render the bag contents page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified products to the shopping bag
    """
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
            else:
                # If item already in bag but not in size:
                bag[item_id]['items_by_size'][size] = quantity
        # If not already in bag, will add item and list by size of items.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            # Updates the quantity if already in bag
            bag[item_id] += quantity
        else:
            # Adds item to the bag if not in bag
            bag[item_id] = quantity

# Overwrites the variable in the session with updated version
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjusts the quantity of the specified products to the shopping bag
    """
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
        else:
            # Remove item if qty = 0
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            """
            If qty is 0, removes the item
            """
            bag[item_id] = quantity
        else:
            # Remove item if qty = 0
            bag.pop(item_id)

    # Overwrites the variable in the session with updated version
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
