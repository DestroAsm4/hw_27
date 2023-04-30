import csv
import json

def to_json():
    with open('categories.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    with open('categories.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)


to_json()