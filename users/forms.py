from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter phone number"
        })
    )

    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your location"
        })
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'phone_number',
            'location',
            'password1',
            'password2'
        ]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Choose a username"
            }),
        }