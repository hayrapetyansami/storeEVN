from django.urls import path

from .views import (
    index, product_details,
    shop, category,
    about, contacts
)

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("product/<slug:slug>", product_details, name="product_details"),
    path("category/<slug:slug>", category, name="category"),
    path("shop/", shop, name="shop"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
]
