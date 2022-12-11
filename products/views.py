from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    View to return all products.
    It includes sorting and search queries.
    """

    products = Product.objects.all()

    # Context is needed because we send something back to the template
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
