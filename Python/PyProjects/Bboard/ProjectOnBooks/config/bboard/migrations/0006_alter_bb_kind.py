# Generated by Django 5.0.7 on 2024-07-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_alter_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю'), ('r', 'Аренда')], default='s', max_length=1, verbose_name='Вид объявлений'),
        ),
    ]