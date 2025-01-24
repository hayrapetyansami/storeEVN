from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category, Slider
from cart.forms import CartAddProductForm


def index(request):
    products = Product.objects.filter(discount__gte=1)
    sliders = Slider.objects.all()

    data = {
        "products": products,
        "sliders": sliders
    }
    return render(request, "main/index.html", data)


def shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 6)
    current_page = paginator.page(int(page))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        paginator = Paginator(products.filter(category=category), 6)
        current_page = paginator.page(int(page))

    data = {
        "category": category,
        "categories": categories,
        "products_qty": products,
        "products": current_page,
    }

    return render(request, "main/shop.html", data)


def category(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.filter(available=True)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 6)
    current_page = paginator.page(int(page))

    data = {
        "categories": categories,
        "category": category,
        "products_qty": products,
        "products": current_page,
    }
    return render(request, "main/category.html", data)


def product_details(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm

    data = {
        "product": product,
        "cart_product_form": cart_product_form
    }
    return render(request, "main/product-details.html", data)


def about(request):
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contacts.html")
