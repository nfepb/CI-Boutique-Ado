from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
    )
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product
from bag.contexts import bag_contents

import stripe


def checkout(request):
    # Payment intent based on Stripe variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        # If form is_valid, save() form
        if order_form.is_valid():
            order_form.save()
            for item_id, item_data in bag.items():
                try:
                    # Get product ID from bag
                    product = Product.objects.get(id=item_id)
                    # Check if item is integer, item does not have sizes
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            # Quantity will be item data
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # If item has sizes, iterate through each size
                        # and create line item accordingly
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                            # In case product is not found:
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

# If user wishes to save their info
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
                )
# If order form is not valid:
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            message.error(
                request, 'There is nothing in your bag at the moment'
                )
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        # Stripe needs amount as integer
        stripe_total = round(total * 100)
        # Set secret key on Stripe
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?'
            )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

# Delete shopping bag from session as no longer needed
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
