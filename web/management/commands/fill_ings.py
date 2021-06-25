from django.core.management.base import BaseCommand, CommandError
from web.models import Recipe

import json

class Command(BaseCommand):
    help = 'Скрипт загрузки ингридентов из json файла'

    def add_arguments(self, parser):
        parser.add_argument('data', type=str)

    def handle(self, *args, **options):
        with open(options['data'], 'rt') as ings_file:
            data = json.load(ings_file)
            for item in data:
                print(item)
        print(Recipe.objects.all())
