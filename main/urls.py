from django.urls import path

from .views import index, product_details

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("product/<slug:slug>", product_details, name="product_details"),
]
