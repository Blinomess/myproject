from django.db import models

class Messages(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активное'),
        ('completed', 'Завершенное'),
    ]
    title=models.CharField('Тема', max_length=50)
    mes_text=models.TextField('Сообщение')
    ent_mail=models.CharField('Почта',max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural='Сообщения'