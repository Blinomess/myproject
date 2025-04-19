from django.db import models
from django.utils import timezone
class Messages(models.Model):
    MES_STATUS=[('new', 'Новое'),
                ('read', 'Прочитано')
                 ]
    TITLE_STATUS=[('Choose theme','Выберите тему'),
                  ('Fire','Пожар'),
                  ('Fire in the forest','Пожар в лесу'),
                  ('Road repairs','Ремонт дорог'), 
                  ('Clean garbage','Убрать мусор'),
                  ('Street light','Уличное освещение'),
                  ('Other','Смотрите тему ниже')]
    title = models.CharField('Тема', max_length=50, choices=TITLE_STATUS, default='Choose theme')
    mes_text=models.TextField('Сообщение', max_length=500)
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