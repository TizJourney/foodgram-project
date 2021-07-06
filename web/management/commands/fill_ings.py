"""
Здесь находится скрипт для начальной загрузки базы ингридентов из файла
Смотри скрипт
fill_ingridients.sh
для запуска этого скрипта
"""

import json

from django.core.management.base import BaseCommand

from web.models import Ingredient


class Command(BaseCommand):
    help = 'Скрипт загрузки ингридентов из json файла'

    def add_arguments(self, parser):
        parser.add_argument('data', type=str)

    def handle(self, *args, **options):
        Ingredient.objects.all().delete()
        with open(options['data'], 'rt') as ings_file:
            data = json.load(ings_file)
            items = [
                Ingredient(title=item['name'], dimension=item['units'])
                for item in data
            ]
            Ingredient.objects.bulk_create(items)
        print(Ingredient.objects.all())
