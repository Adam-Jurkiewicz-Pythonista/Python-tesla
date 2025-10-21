import json

file_name = "plik_danych.json"
with open(file_name, 'r') as pliczek:
    dane = json.load(pliczek)

print(json.dumps(dane, indent=4))