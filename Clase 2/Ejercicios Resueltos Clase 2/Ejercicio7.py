print("Hola amigo, vamos a jugar que soy Carl Friedrich Gauss y vos sos el profesor que nos dice qué números sumar")
n = int(input("Tirame un número y te digo cuánto es la suma desde el 1 hasta este: "))
for i in range (1, n + 1):
    suma = (n * (n + 1)) / 2

print(f"El total es {suma}... tomá pa'vos! jeje")