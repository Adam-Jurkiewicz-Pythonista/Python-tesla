def fn_licz(a,b):
    return a+b

def fn_licz2(a,b):
    if b == 0:
        return False

    wynik1 = a+b
    wynik2 = a/b
    return (wynik1, wynik2, str(wynik1)+"w")

wyn = fn_licz2(2,3)
print(wyn)

a,b,c = fn_licz2(3,0)

print(a)
print(b)
print(c)

