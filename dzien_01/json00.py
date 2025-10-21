import json

dane = {
    "name": "Dane",
    "imie": "Adaś",
}
print(json.dumps(dane))
print(json.dumps(dane,ensure_ascii=False))
print(dane)
