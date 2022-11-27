from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Nome de usuário'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'E-mail de contato'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Confirmar senha'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
