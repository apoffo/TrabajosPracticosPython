print("Amigo, me alegro por tu herencia pero una lástima que se haya muerto tu bistatara Abuelo! 138 años!!... re joven!!")
print("Vamos a hacer una cosa...")
herencia = int(input("Decime... cuánto es el monto que tenés para invertir?:"))
# Cn = Co * (1 + i)**n Fórmula de Interés compuesto
# donde Cn es el Capital final en el año "n"
# Co es el capital inicial
# i es la tasa de interés
# n es el perído del ahorro en años
plazo_fijo_en_5_anios = round(herencia * (1 + 0.5) ** 5 , 2) 
bonos_y_acciones = round(herencia * (1 + 0.25) ** 5*2 , 2)
print("Ok, tenés plazo fijo con 0.5 anual y Bonos y divisas 0.25 semestral")
print("Te tiro los datos")
print(f"plazo fijo: {plazo_fijo_en_5_anios}")
print(f"Bonos y acciones: {bonos_y_acciones}")
if plazo_fijo_en_5_anios > bonos_y_acciones:
    print("El plazo fijo te deja más, te conviene!")
else:
    print("Los bonos te convienen!")

