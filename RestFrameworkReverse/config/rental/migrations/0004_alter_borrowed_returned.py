# Generated by Django 5.0.3 on 2024-03-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_borrowed_what'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='returned',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата'),
        ),
    ]