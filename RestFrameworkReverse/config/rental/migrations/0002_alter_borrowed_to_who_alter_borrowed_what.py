# Generated by Django 5.0.3 on 2024-03-23 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='to_who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.friend', verbose_name='Для кого'),
        ),
        migrations.AlterField(
            model_name='borrowed',
            name='what',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.belonging', verbose_name='Почему'),
        ),
    ]
