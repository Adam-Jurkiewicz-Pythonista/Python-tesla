# tu chcemy wykorzystać funkcje

# plik o nazwie funkcje.py musi być w tym samym katalogu
from funkcje import *

while True:
    passwd = input("Podaj hasło (END) :")
    if passwd == "END":
        break
    _, hash = hash_password(passwd)
    print(f"Zaszyfrowane hasło: {hash=}")
