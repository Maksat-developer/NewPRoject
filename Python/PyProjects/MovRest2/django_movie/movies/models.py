from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    url = models.CharField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='actors/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    url = models.CharField(max_length=160, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заглавление')
    tagline = models.CharField(
        max_length=100,
        verbose_name='Слоган',
        default='')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(verbose_name='Постер', upload_to='movies/', blank=True, null=True)
    year = models.PositiveSmallIntegerField(
        verbose_name='Дата выхода', default=2019)
    country = models.CharField(verbose_name='Страна', max_length=50)
    directors = models.ManyToManyField(
        Actor,
        verbose_name='Режиссер',
        related_name='film_director')
    actors = models.ManyToManyField(
        Actor,
        verbose_name='Актеры',
        related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    world_premiere = models.DateField(
        verbose_name='Премьера в мире',
        default=date.today)
    budget = models.PositiveIntegerField(
        verbose_name='Бюджет',
        default=0,
        help_text='Указывать сумму в доллорах')
    fees_in_usa = models.PositiveIntegerField(
        verbose_name='Сборы в США',
        default=0,
        help_text='Указывать сумму в доллорах')
    fees_in_world = models.PositiveIntegerField(
        verbose_name='Сборы в мире',
        default=0,
        help_text='Указывать сумму в доллорах')

    category = models.ForeignKey(Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, blank=True, null=True, unique=True,)
    draft = models.BooleanField(verbose_name='Черновик', default=False)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='movie_shots/')
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='Фильм')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(
        verbose_name='Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинка'
        verbose_name_plural = 'Звезды рейтинка'


class Rating(models.Model):
    ip = models.CharField(verbose_name='IP-адрес', max_length=20)
    star = models.ForeignKey(
        RatingStar,
        on_delete=models.CASCADE,
        verbose_name='звезда')
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='фильм')

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(verbose_name='Имя', max_length=100)
    text = models.TextField(verbose_name='Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self',
        verbose_name='Родитель',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='фильм')

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
