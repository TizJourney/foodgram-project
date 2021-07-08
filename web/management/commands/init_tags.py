"""
Здесь находится скрипт для начальной загрузки в базу списка тегов для фильтрации
"""

from django.core.management.base import BaseCommand

from web.models import RecipeTag


class Command(BaseCommand):
    help = 'Скрипт загрузки фильтров рецепта'

    def handle(self, *args, **options):
        RecipeTag.objects.all().delete()
        items = [
            RecipeTag(slug='breakfast', name='Завтрак', color='orange'),
            RecipeTag(slug='lunch', name='Обед', color='green'),
            RecipeTag(slug='dinner', name='Ужин', color='purple'),
        ]
        RecipeTag.objects.bulk_create(items)
        total_count = RecipeTag.objects.count()
        print(f'Добавлено {total_count} объектов')
