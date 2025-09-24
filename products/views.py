from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
    Simple view to return products page, including sorting and search queries.
    """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if "category" in request.GET:
            category = request.GET["category"].split(",")
            products = products.filter(category__name__in=category)
            categories = Category.objects.filter(name__in=category)



        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Sorry, we couldnt fine that item, try again!")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "chosen_categories": category,
    }

    return render(request, "products/products.html", context)





def product_details(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}

    return render(request, "products/product_details.html", context)
