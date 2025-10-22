def funkcja_licz(a,b):
    if b == 0:
        return (False, 0)
    wynik1 = a+b
    wynik2 = a/b
    return (True, (wynik1, wynik2) )

ok, wartosc = funkcja_licz(2,3)
if ok:
    print(wartosc)
    a,b = wartosc
    print(a,b)

ok, wartosc = funkcja_licz(2,0)
if ok == True:
    print(wartosc)