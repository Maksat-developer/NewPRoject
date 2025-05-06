from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    date_posted = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    title = models.TextField(verbose_name='Описание')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return f'Автор: {self.author} Контент: {self.content}'
    

    class Meta: 
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

