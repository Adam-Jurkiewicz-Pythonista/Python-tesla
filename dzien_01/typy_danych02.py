# lista wielowymiarowa

lista = [ [1,11] , [2,22], [3,33] ]
print(lista)
print(lista[0])
print(lista[0][1])
lista = lista + [ [4,44], 555555 ]
print(lista)

# iteracja, po każdym elemencie listy
for element in lista:
    print(f"Dla {element=} {type(element)=}")