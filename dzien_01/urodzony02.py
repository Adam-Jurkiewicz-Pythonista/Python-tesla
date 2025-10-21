def read_data_from_keyboard():
    temp = "NIC"
    while temp.isdigit() is False:
        temp = input("Podaj dane cyfrowe :")

    return int(temp)

imie = input("Podaj swoje imie: ")
rok_urodzenia = read_data_from_keyboard()
aktualny_rok = 2025
wiek = aktualny_rok - rok_urodzenia
print("Imie: {imie}")
print(f"Imie: {imie}")
print(f"{imie} ma w roku {aktualny_rok} {wiek} lat.")