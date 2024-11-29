from django.db import models
from django.contrib.auth.models import User


# Запчасти к Объявлениям 
class Spare(models.Model):
    name = models.CharField(max_length=30, verbose_name='Запчасти')

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    def __str__(self) -> str:
        return self.name
    



#  Пользователь 
class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Пользовтель'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.user


# Рубрика


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Название',
        db_index=True)

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self):
        return self.name

# Меры измерения


class Measure(models.Model):
    class Measurements(float, models.Choices):
        METERS = 1.0, 'Метры'
        FEET = 0.3048, 'Футы'
        YARDS = 0.9144, 'Ярды'

    measurement = models.FloatField(choices=Measurements.choices)

    def __str__(self) -> str:
        return str(self.measurement)

    class Meta:
        verbose_name = 'Мера'
        verbose_name_plural = 'Меры измерения'

# Класс Объявления


class Bb(models.Model):
    class Kinds(models.TextChoices):
        BUY = 'b', 'Куплю'
        SELL = 's', 'Продам'
        EXCHANGE = 'c', 'Обменяю'
        RENT = 'r', 'Аренда'

    kind = models.CharField(
        max_length=1,
        verbose_name='Вид объявлений',
        choices=Kinds.choices,
        default=Kinds.SELL)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    


# ссылка на функцию, не принимающую параметров и воз­вращающую значение,
# которое будет записано в поле:


    def get_first_rubric():
        return Rubric.objects.first()
    

    spare = models.ManyToManyField(Spare, verbose_name='Запчасти')

    rubric = models.ForeignKey(
        Rubric,
        null=True,
        on_delete=models.SET(get_first_rubric),
        verbose_name='Рубрика')
    measure = models.ForeignKey(
        Measure,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Меры измерения')
    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published','title']
        
