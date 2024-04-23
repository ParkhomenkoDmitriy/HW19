import csv
import json
import random

with open("D:/people_dict.json", 'r', encoding='utf-8') as json_file:
    people = json.load(json_file)

operators = ['095', '066', '098', '096', '050', '097']

people_with_phones = []

for key, value in people.items():
    has_phone = random.random() < 0.75
    phone_number = (random.choice(operators) + "".join(random.choices("0123456789", k=7))) if has_phone else ""

    people_with_phones.append({
        "ID": key,
        "Имя": value[0],
        "Возраст": value[1],
        "Телефон": phone_number,
    })

with open("D:/people_with_phones.csv", 'w', newline='', encoding='utf-8-sig') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["ID", "Имя", "Возраст", "Телефон"], delimiter=',')
    csv_writer.writeheader()
    csv_writer.writerows(people_with_phones)

print(people_with_phones)
