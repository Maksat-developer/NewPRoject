from distutils.command.upload import upload
from email.policy import default
from tkinter.tix import Tree
from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=200)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=0)
    descriptions = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to = 'actors/%Y/%m/%d')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Актёр и режисёр'
        verbose_name_plural = 'Актёры и режисёры'



class Genre(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    descriptions = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'



class Movie(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    tagline = models.CharField(verbose_name="Слоган", max_length=150, default='')
    descriptions = models.TextField(verbose_name='Описание')
    poster = models.ImageField(verbose_name='Постер', upload_to='movie/%Y/%m/%d')
    year = models.PositiveSmallIntegerField(verbose_name='Дата выхода', default=2019)
    country = models.CharField(verbose_name='Страна', max_length=200)
    directors = models.ManyToManyField(Actor, verbose_name='режиссёр', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актёры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premieres = models.DateField(verbose_name='Примьера в мире', default=date.today)
    budget = models.PositiveIntegerField(verbose_name='Бюджет', default=0, help_text='Указывать сумму в доллорах')
    fees_in_usa = models.PositiveIntegerField(
        verbose_name ='Сборы в США', default=0, help_text='Указывать сумму в доллорах'
        )

    fees_in_world = models.PositiveIntegerField(
        verbose_name ='Сборы в мире', default=0, help_text='Указывать сумму в доллорах'
        )
    
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)

    
    url = models.SlugField(max_length=200, unique=True)
    draft = models.BooleanField(verbose_name='Черновик', default=False)


    def __str__(self):
        return f"{self.title} - {self.tagline}"
        


    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"slug": self.url})


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):

    title = models.CharField(verbose_name='Заголовок', max_length=150)
    descriptions = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='movie_shots/%Y/%m/%d')
    movie = models.ForeignKey(Movie, verbose_name='Фильмы', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильмов'


    
class RetingStar(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name="значение", default=0)


    def __str__(self):
        return self.value


    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звёзды рейтинга'

    




class Reting(models.Model):
    ip = models.CharField(verbose_name='IP адресс', max_length=15)
    star = models.ForeignKey(RetingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f"{self.star} - {self.movie}"


    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(verbose_name='Имя', max_length=100)
    text = models.TextField(verbose_name='Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм', related_name="reviews")


    def __str__(self):
        return f'{self.name} - {self.movie}'


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'







    





