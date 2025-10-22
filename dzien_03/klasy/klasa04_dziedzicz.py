class Statek:
    def __init__(self, nazwa: str):
        print(f"Initializing Statek: {nazwa}")
        self.nazwa = nazwa

    def daj_info(self):
        return f"Daj info o: {self.nazwa}"

class Zaglowiec(Statek):
    pass


orp_orzel = Statek("orp orzeł")
cutty = Zaglowiec("Cutty Sark")
print(orp_orzel)
print(orp_orzel.daj_info())
print(dir(orp_orzel))
print('---------------')
print(cutty)
print(dir(cutty))
print(cutty.daj_info())
