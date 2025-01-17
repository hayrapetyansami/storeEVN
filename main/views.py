from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Slider


def index(request):
    products = Product.objects.filter(discount__gte=1)
    sliders = Slider.objects.all()

    data = {
        "products": products,
        "sliders": sliders
    }
    return render(request, "main/index.html", data)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    data = {
        "product": product
    }
    return render(request, "main/product-details.html", data)


def shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    data = {
        "category": category,
        "categories": categories,
        "products": products
    }

    return render(request, "main/shop.html", data)


def category(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(available=True)
    data = {
        "categories": categories,
        "category": category,
        "products": products
    }
    return render(request, "main/category.html", data)


def about(request):
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contacts.html")
