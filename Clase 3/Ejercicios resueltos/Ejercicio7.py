#Ejercicio 7
palabra = input("Querés que te cuente el cuento de la buena pipa?: ")

while palabra != "salir":
    palabra = input(f"Yo no te dije \"{palabra}\"... te dije si querés que te cuente el cuento de la buena pipa?: ")
    if palabra == "salir":
        break

print("Me divertí con tigo")
