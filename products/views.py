from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    View to return all products.
    It includes sorting and search queries.
    """

    products = Product.objects.all()
    query = None

    """
    To match term in either product name or description through queries
    """
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Context is needed because we send something back to the template
    context = {
        'products': products,
        'search_term': query
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
