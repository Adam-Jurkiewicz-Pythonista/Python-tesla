class Statek:
    def __init__(self, nazwa: str, rodzaj: str):
        print(f"Initializing Statek: {nazwa}")
        print("Rownież super wykona..")
        self.super = True
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def daj_info(self):
        return f"Daj info o: {self.nazwa} - {self.rodzaj}"

# super - metoda pythonowa dobra
class Zaglowiec(Statek):
    def __init__(self, nazwa_statku):
        super().__init__(nazwa_statku, "Zaglowiec")

    def daj_info(self):
        return f"Tylko żaglowiec: {self.nazwa}"

# bez super - niezbyt ładne, choć działa
class Podwodny(Statek):
    def __init__(self, nazwa_statku):
        self.nazwa = nazwa_statku
        self.rodzaj = "Podwodny"

inny = Statek("inny", "jakiś tam")
print(dir(inny))
orp_orzel = Podwodny("orp orzeł")
cutty = Zaglowiec("Cutty Sark")
print(orp_orzel)
print(orp_orzel.daj_info())
print(dir(orp_orzel))
print('---------------')
print(cutty)
print(dir(cutty))
print(cutty.daj_info())
