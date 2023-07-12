def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i] 
        i += 1
    promedio = suma / i
    print (promedio)

lista = [3,5,8,6,3]

promedio(lista)

   