# Generated by Django 3.0.5 on 2021-07-08 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20210708_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipetag',
            options={'verbose_name': 'Тег рецепта', 'verbose_name_plural': 'Теги рецепта'},
        ),
    ]
