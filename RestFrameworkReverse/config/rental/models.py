from django.db import models



class Friend(models.Model):
    name = models.CharField(max_length=10, verbose_name='Имя друга')

    def __str__(self):
        return self.name


class Belonging(models.Model): # Принадлежность
    name = models.CharField(max_length=100, verbose_name="Кому принадлежит")

    def __str__(self):
        return self.name



class Borrowed(models.Model): # Заимствованный
    what = models.ForeignKey(Belonging, verbose_name="Принадлежит", on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, verbose_name='Для кого', on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True, verbose_name="Дата Займа")
    returned = models.DateTimeField(verbose_name='Дата возврата',null=True, blank=True)

    def __str__(self):
        return self.to_who
