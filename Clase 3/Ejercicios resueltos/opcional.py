#Ejercicio opcional
print("Vamos a hacer un triángulo rectángulo con los números que me des, vamos?")
num1 = int(input("Decime un número entero: "))
lista = []
lista_reves = []
otralista = []
for i in range(1, num1 + 1, 2):
    lista.append(i)
    print (lista)
print()

print("Al revés sería:")
#al revés
for i in range(1, num1 + 1, 2):
    lista_reves.insert(0,i)
    print (lista_reves)
    
print()
print("Y sino será así")
for i in range(1, num1 + 1, 2):
    otralista.append(i)
    otralista.sort()
    otralista.reverse()
    print (otralista)
    
print()
print("listo")    
