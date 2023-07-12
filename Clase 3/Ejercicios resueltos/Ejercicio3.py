#Ejercicio 3
contrasenia = int(input("Ingrese su contraseña numérica de 6 digitos: "))

contador = 0
while contrasenia != 123456:
     contador += 1
     if contador < 2:
         print("no... esa no es, volvé a ingresarla")
     elif contador == 2:
         print("es la segunda vez que te equivocas, pensá de nuevo y volvé a ingresarla")
     elif contador == 3:
         print("estás mal de memoria? mirá que te bloqueo. Fijate donde la anotaste")
     elif contador == 4:
         print("¿Cuántas veces te vas a confundir? son 6 números nomás!!Preguntale a alguien si se acuerda y volvé a ingresarla")
     elif contador == 5:
         print("Ya me estás cayendo mal... ya te dije, la próxima te bloqueo")
     elif contador == 6:
         print("Bloqueado! me cansaste!")
     else:
         print("Vení el lunes a blanquear la clave")
         break
     contrasenia = int(input("Ingrese su contraseña numérica de 6 digitos: "))

if contador > 1:
    print(f"Te confundiste {contador} veces! hay que comer más pescado para la memoria")
else:
    print("Acceso concedido")

    
