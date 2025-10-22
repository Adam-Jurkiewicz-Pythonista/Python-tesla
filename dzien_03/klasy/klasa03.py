class Statek:
    def __init__(self, nazwa: str):
        print(f"Initializing Statek: {nazwa}")
        self.nazwa = nazwa

    def daj_info(self):
        return f"Daj info o: {self.nazwa}"


orp_orzel = Statek("orp orzeł")
print(orp_orzel)
print(orp_orzel.daj_info())
print(dir(orp_orzel))
