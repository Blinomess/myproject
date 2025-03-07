from .models import Messages
from django.forms import ModelForm, TextInput, Textarea

class MessagesForm(ModelForm):
    class Meta:
        model=Messages
        fields=['title', 'mes_text', 'ent_mail']
        widgets={
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Тема сообщения',
                'required': 'required'
            }),
            'ent_mail': TextInput(attrs={
                'class':'form-control',
                'placeholder':'вашапочта@mail.ru (пример)',
                'required': 'required'
            }),
            'mes_text': Textarea(attrs={
                'class':'form-control',
                'style':'min-height: 100px; max-height: 300px;',
                'placeholder':'Опишите вашу проблему',
                'required': 'required'
            })
        }