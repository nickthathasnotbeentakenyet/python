from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Статья')
    date = models.DateTimeField('Дата')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta: # для отображения названий моделей в панели админа
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        