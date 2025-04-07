from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'style': 'width: 400px; margin-left: 39.9%',
        'placeholder': 'Логин'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'style': 'width: 400px; margin-left: 39.9%',
        'placeholder': 'Пароль' 
        }))