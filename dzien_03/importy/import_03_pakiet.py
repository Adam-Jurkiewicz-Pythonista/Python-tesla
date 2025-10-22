# tu chcemy wykorzystać funkcje

# plik z funkcjami o nazwie szyfrowanie w pakiecie dodatki
from dodatki.szyfrowanie import *

while True:
    passwd = input("Podaj hasło (END) :")
    if passwd == "END":
        break
    _, hash = hash_password(passwd)
    print(f"Zaszyfrowane hasło: {hash=}")
    # od razu sprawdzenie rozszyfrowania
    xxx = verify_password(...)
    print(f"Poprawne? {xxx}")
