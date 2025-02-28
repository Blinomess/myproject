from .models import Login
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput

class LoginForm(AuthenticationForm):
    class Meta:
        model=Login
        fields=['login','password']
        widgets={
            'login': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Логин'
            }),
            'password': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Пароль'
            })
        }