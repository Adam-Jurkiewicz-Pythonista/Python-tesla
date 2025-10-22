def fnsum(a: int, b: int) -> int:
    """
    suma dwóch elementów
    :param a: musi być str
    :param b:
    :return: a+b
    """
    return a + b


wynik = fnsum(1,2)
print(wynik)
# wynik = fnsum("aa",12)
print(wynik)

wynik = fnsum("ada","sssss")
print(wynik)