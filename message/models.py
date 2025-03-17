from django.db import models

class Messages(models.Model):
    MES_STATUS=[('new', 'Новое'),
                ('read', 'Прочитано')
                 ]
    title=models.CharField('Тема', max_length=50)
    mes_text=models.TextField('Сообщение')
    ent_mail=models.CharField('Почта',max_length=50)
    latitude = models.FloatField('Широта', default='0.0')
    longitude = models.FloatField('Долгота', default='0.0')
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=5, choices=MES_STATUS, default='new')  
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural='Сообщения'