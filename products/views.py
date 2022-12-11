from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """
    View to return all products.
    It includes sorting and search queries.
    """

    products = Product.objects.all()
    query = None
    categories = None

    """
    To match term in either product name or description through queries
    """

    if request.GET:
        # To capture the category parameter through foreign key thanks to "__":
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # To capture the query input:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
                )
            products = products.filter(queries)

    # Context is needed because we send something back to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
