def cuadrado(lista):
    otra = []
    for i in range(len(lista)):
        otra.append(lista[i] ** 2) 
        i += 1
    return otra

lista = [3,5,8,6,4]

print(cuadrado(lista))