
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)


    def __str__(self):
        return self.name


class SubCategories(models.Model):
    name =  models.CharField(verbose_name="Название подкатегории", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    tittle = models.CharField(verbose_name="Заглавление", max_length=100)
    descriptions = models.TextField(verbose_name="Описание обьявления")
    category = models.ManyToManyField(Category)
    sub_category = models.ManyToManyField(SubCategories)
    image = models.ImageField(verbose_name="Изображение", upload_to="media/Y%/m%/%d")
    data_published = models.DateTimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return str(f"{self.tittle} - {self.data_published}")
    