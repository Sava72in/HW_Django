import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('/Users/macbookair/Desktop/Netology/HW_Django/dj-homeworks/2.1-databases/work_with_database/phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            set_info = Phone(id=phone.get('id'),
                             name=phone.get('name'),
                             image=phone.get('image'),
                             price=phone.get('price'),
                             release_date=phone.get('release_date'),
                             lte_exists=phone.get('lte_exists'),
                             slug=phone.get('name'))
            set_info.save()
