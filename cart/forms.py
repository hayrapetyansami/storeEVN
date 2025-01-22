from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedMultipleChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    overried = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
