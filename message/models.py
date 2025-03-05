from django.db import models

class Messages(models.Model):
    title=models.CharField('Тема', max_length=50)
    mes_text=models.TextField('Сообщение')
    ent_mail=models.CharField('Почта',max_length=50)
    def __str__(self):
        return self.title
    