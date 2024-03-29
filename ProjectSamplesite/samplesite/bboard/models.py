from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    class Meta:
        verbose_name = 'Рубрики'
        verbose_name_plural = 'Рубрика'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Bboard(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    rubric = models.ForeignKey(
        Rubric,
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика')
    published = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Опубликовано',
        db_index=True)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявление'
        ordering = ['-published']

    def __str__(self):
        return self.title
