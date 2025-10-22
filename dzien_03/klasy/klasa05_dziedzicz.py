class Statek:
    def __init__(self, nazwa: str, rodzaj: str):
        print(f"Initializing Statek: {nazwa}")
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def daj_info(self):
        return f"Daj info o: {self.nazwa} - {self.rodzaj}"

class Zaglowiec(Statek):
    pass


orp_orzel = Statek("orp orzeł", "podwodny")
cutty = Zaglowiec("Cutty Sark", "zaglowiec")
print(orp_orzel)
print(orp_orzel.daj_info())
print(dir(orp_orzel))
print('---------------')
print(cutty)
print(dir(cutty))
print(cutty.daj_info())
