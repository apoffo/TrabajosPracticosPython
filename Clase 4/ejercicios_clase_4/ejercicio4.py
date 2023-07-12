def total(precio, porcentaje):
    iva = precio * (porcentaje/100)
    precio = precio + iva
    return precio

precio = float(input("Ingrese el valor del producto: "))
porcentaje = float(input("Ingrese el porcentaje de IVA: "))

print(total(precio, porcentaje))
