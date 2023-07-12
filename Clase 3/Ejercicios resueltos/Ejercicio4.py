#Ejercicio 4
print("Vamos a preparar un pancito? Dale!")
harina = float(input("Decime cuántos Kg tenés de harina: "))
azucar = float(input("Cuántos kg de azucar tenés?: "))
manteca = float(input("Y de manteca, cuántos Kg tenés?: "))

if harina == 5:
    print("De harina estás bien!")
elif harina < 5:
    print(f"No te alcanzan {harina} kg de harina, andá a comprar {5-harina} kg más!")
else:
    print(f"Tenes {harina-5} kg de más. Necesitas solo 5 Kg")

if azucar == 1:
    print("De azucar estás bien!")
elif azucar < 1:
    print(f"No te alcanzan {azucar} kg de azucar, andá a comprar {1-azucar} kg más!")
else:
    print(f"Tenes {azucar-1} kg de más. Necesitas solo 1 Kg.")

if manteca == 2:
    print("De manteca estás bien!")
elif manteca < 2:
    print(f"No te alcanzan {manteca} kg de manteca, andá a comprar {2-manteca} kg más!")
else:
    print(f"Tenes {manteca-2} kg de más. Necesitas solo 2 Kg")

if harina == 5 and azucar == 1 and manteca == 2:
    print("Manos a la obra... dale que tengo hambre!")
else:
    print("Ya te dije cuánto lleva la preparación")
