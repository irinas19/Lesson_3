#Задача - ввести из этого файла все имена и координаты вертолетных аэропортов

import json

with open('airport-codes_json.json', 'r') as airport_file:
    airport_data = json.load(airport_file)
    for item in airport_data:
        print(item['name'], item['coordinates'])
