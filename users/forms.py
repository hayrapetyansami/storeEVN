from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, UserChangeForm
)
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    address = forms.CharField()
    postal_code = forms.CharField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "country",
            "city",
            "address",
            "postal_code",
        )


class ProfileForm(UserChangeForm):
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    country = forms.CharField()
    city = forms.CharField()
    address = forms.CharField()
    postal_code = forms.CharField()

    class Meta:
        model = User
        fields = (
            "avatar",
            "first_name",
            "last_name",
            "username",
            "email",
            "country",
            "city",
            "address",
            "postal_code",
        )
