from django.contrib import admin

from .models import Order, OrderItem
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


def order_stripe_payment(obj):
    print(obj.stripe_id)
    if obj.stripe_id:
        url = f'https://dashboard.stripe.com/payments/{obj.stripe_id}'
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return '-'

order_stripe_payment.short_description = "Stripe Payment"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id", "first_name", "last_name", "email",
        "paid", "country", "city", "address", order_stripe_payment,
        "postal_code", "created", "updated"
    ]

    list_display_links = ["first_name", "last_name", "email"]
    list_filter = ["paid", "country", "city", "created", "updated"]
    search_fields = ["first_name", "last_name",
                     "email", "address", "postal_code"]
    inlines = [OrderItemInline]
