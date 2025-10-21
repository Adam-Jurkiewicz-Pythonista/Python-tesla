# słownik - lista hashująca

slownik = { 10: "Beata1", 2: "Beata2", "C": "Adam",
            "ABC": 53534534534,
            "CDE": [4 , 5, [33, 'AAA'] ]}
print(slownik)
for element in slownik:
    print(f"{element=}")
    print(f"{slownik[element]=}")