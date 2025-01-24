from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="categories/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="products/", blank=True)
    descr = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(
        default=0.00,
        max_digits=4,
        decimal_places=2
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="products"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_details", args=[self.category.slug, self.slug])

    def discount_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created_at"]),
        ]
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Slider(models.Model):
    name = models.CharField(max_length=255)
    descr = models.TextField()
    image = models.ImageField(upload_to="slider/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["-created_at"]),
        ]
        verbose_name = "Slider Item"
        verbose_name_plural = "Slider Items"
