print("Ok, ya falta poco para terminar, vamos con otra fácil")
n1 = int(input("Decime un número: "))
n2 = int(input("Ahora decime otro número: "))
print("Bien... ahora vas a ver una división entera y otra división común")
division_entera = round(n1 // n2, 2)
division_comun = round(n1 / n2, 2)
print(f"Esto es el resultado de la división entera: {division_entera}")
print(f"Y esto es el resultado de la división común: {division_comun}")