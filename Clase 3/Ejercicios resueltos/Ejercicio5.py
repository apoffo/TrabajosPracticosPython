#Ejercicio 5
print("Bienvenidos al parque de diversiones \"Me Caigo de Risa\"")
edad = int(input("Mencione su edad y yo le digo cuánto tiene que pagar: "))

if edad < 2:
    print("ah-gu-gu-da-da... Los menores no pagan, cuide el chupete")
elif edad > 2 and edad <= 4:
    print("Chico/a pidale $100 al pa o a la ma")
elif edad > 4 and edad <= 10:
    print("Pague $200 a la Bati chica para entrar")
elif edad > 10 and edad <= 18:
    print("Vamo'... poniendo $400 para entrar...")
elif edad > 18 and edad <= 65:
    print("Con una luquita pase nomás")
elif edad > 65:
    print("Jubilados pagan $500")

print("Gracias por su visita!")
