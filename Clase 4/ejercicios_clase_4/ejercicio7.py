def lista_solo_pares(lista):
    otra = []
    for i in range(len(lista)):
        valor = lista[i] % 2
        if valor == 0:
            otra.append(lista[i]) 
        i += 1
    return otra

lista = [3,5,8,6,4,3,1,7,5,4,8,2,3]

print(lista_solo_pares(lista))