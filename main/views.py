from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request):
    products = Product.objects.filter(available=True)

    data = {
        "products": products
    }
    return render(request, "main/index.html", data)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    data = {
        "product": product
    }
    return render(request, "main/product-details.html", data)
