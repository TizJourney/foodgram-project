# Generated by Django 3.0.5 on 2021-06-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20210623_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузка изображения. Опционально.', null=True, upload_to='media/', verbose_name='Загрузить фото'),
        ),
    ]