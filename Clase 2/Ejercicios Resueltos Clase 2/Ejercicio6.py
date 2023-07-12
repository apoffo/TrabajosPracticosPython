print("Hola pibe... esto es un cálculo para la inclusión")
n1 = int(input("Decime un número: "))
n2 = int(input("Ahora decime otro número: "))

# n1 = 7
# n2 = 12
# 8 + 9 + 10 + 11 
# suma n1 + 1 hasta n1 < n2 => suma = 8+9+10+11 => 38
# suma = n2 + 1 desde n1 hasta n2 => suma = 7+8+9+10+11+12 => 57
sume_inclusive = 0
num2 = n2 + 1
for nobinario in range(n1, num2):
    sume_inclusive += nobinario

print(f"Le sume desde {n1} hasta {n2} inclusive es de: {sume_inclusive}")

suma_retrograda = 0
num1 = n1 + 1
for x in range(num1, n2):
    suma_retrograda += x

print(f"El resultado de la suma es: {suma_retrograda}")
