from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
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

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MHs3yAkzgggt5AOxq5ttOAIsawRyEF6xRdAUwfsOlLNYjaNauPPmTwQCTYWJirPwnrNGbkRzxbpzM14uLizSS3a00pYGFj3DZ',
        'client_secret': 'myvery_secret_key',
    }

    return render(request, template, context)
