from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    View to return specific product with details.
    """

    product = get_object_or_404(Product, pk=product_id)

    # Context is needed because we send something back to the template
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
