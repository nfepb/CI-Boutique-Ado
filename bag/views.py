from django.shortcuts import render, redirect


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
    # If there is a bag variable in the session, adds to dictionnary,
    # if not, creates one
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # Updates the quantity if already in bag
        bag[item_id] += quantity
    else:
        # Adds item to the bag if not in bag
        bag[item_id] = quantity

# Overwrites the variable in the session with updated version
    request.session['bag'] = bag
    return redirect(redirect_url)
