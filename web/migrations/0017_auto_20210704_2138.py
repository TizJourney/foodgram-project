# Generated by Django 3.0.5 on 2021-07-04 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20210704_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='ingredientquanity',
            name='ingridients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='web.Ingredient', verbose_name='ингридиент'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredientquanity',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='web.Recipe', verbose_name='Рецепт'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='ingredientquanity',
            unique_together={('recipe', 'ingridients')},
        ),
        migrations.RemoveField(
            model_name='ingredientquanity',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ingredientquanity',
            name='units',
        ),
    ]