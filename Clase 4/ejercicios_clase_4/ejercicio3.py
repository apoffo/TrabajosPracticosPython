def factorial(num):
    if num <= 1:
        return  1
    resultado = num * factorial(num-1)
    return resultado
numero = int(input("Ingrese un número: "))

print(factorial(numero))
