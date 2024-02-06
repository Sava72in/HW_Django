import csv


def handle(*args, **options):
    with open('phones.csv', 'r') as file:
        phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            id = phone.get('id')
            name = phone.get('name')
            image = phone.get('image')
            price = phone.get('price')
            release_date = phone.get('release_date')
            lte_exists = phone.get('lte_exists')

handle()