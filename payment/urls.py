from django.urls import path
from .views import payment_process, payment_completed, payment_cancelled
from .webhooks import stripe_webhook

app_name = "payment"

urlpatterns = [
    path("process/", payment_process, name="process"),
    path("completed/", payment_completed, name="completed"),
    path("cancelled/", payment_cancelled, name="cancelled"),
    path("webhook/", stripe_webhook, name="webhook"),
]