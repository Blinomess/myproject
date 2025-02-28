from django.db import models

class Login(models.Model):
    login=models.CharField('Логин', max_length=50)
    password=models.CharField('Пароль',max_length=50)
    def __str__(self):
        return self.title
    