from django.db import models

class message_form(models.Model()):
    title=models.CharField('Тема', max_length=50)
    text=models.TextField('Сообщение')
    entmail=models.CharField('Почта',max_length=50)
    def _str_(self):
        return self.title
    