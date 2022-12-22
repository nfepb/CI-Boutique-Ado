from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(
            request, 'There is nothing in your bag at the moment'
            )
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'id_stripe_public_key': 'pk_test_51MHs3yAkzgggt5AOxq5ttOAIsawRyEF6xRdAUwfsOlLNYjaNauPPmTwQCTYWJirPwnrNGbkRzxbpzM14uLizSS3a00pYGFj3DZ',
        'client_secret': 'myvery_secret_key',
    }

    return render(request, template, context)
