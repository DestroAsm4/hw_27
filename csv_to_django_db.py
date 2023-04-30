import csv
from ads.models import ADS, Categories

with open('categories.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    print(rows)
    for row in rows:
        _, created = Categories.objects.get_or_create(
                        name=row['name'],
                        )

with open('ads.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    for row in rows:
        _, created = ADS.objects.get_or_create(
                        name=row['name'],
                        author=row['author'],
                        price=row['price'],
                        description=row['description'],
                        address=row['address'],
                        is_published=row['is_published'],
                        )
