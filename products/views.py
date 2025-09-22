from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """
    Simple view to return products page, including sorting and search queries.
    """

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "products/products.html", context)
