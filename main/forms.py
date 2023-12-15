from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Receipt
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username","email","password1",'password2']


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["store","item",'total_amount']