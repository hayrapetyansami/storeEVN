from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        if self.request.user.is_authenticated:
            self.initial["first_name"] = self.request.user.first_name
            self.initial["last_name"] = self.request.user.last_name
            self.initial["email"] = self.request.user.email
            self.initial["country"] = self.request.user.country
            self.initial["city"] = self.request.user.city
            self.initial["address"] = self.request.user.address
            self.initial["postal_code"] = self.request.user.postal_code

    def save(self, commit=True):
        order = super().save(commit=False)
        order.user = self.request.user
        if commit:
            order.save()
        return order

    class Meta:
        model = Order
        fields = [
            "user", "first_name", "last_name", "email",
            "country", "city", "address", "postal_code"
        ]
