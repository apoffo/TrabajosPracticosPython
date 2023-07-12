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
plazo_fijo_mensual = round(round(herencia * (1 + 0.035) ** 5*12 , 2))
print("Ok, tenés plazo fijo con 0.5 anual y Bonos y divisas 0.25 semestral")
print("Te tiro los datos")
print(f"plazo fijo: {plazo_fijo_en_5_anios}")
print(f"Bonos y acciones: {bonos_y_acciones}")
print("A tu amigo que te dijo que te convenia el plazo de fijo a tasa mensual, te los paso de nuevo")
print(f"y el plazo fijo mensual es: {plazo_fijo_mensual}")
if plazo_fijo_en_5_anios > bonos_y_acciones and plazo_fijo_en_5_anios > plazo_fijo_mensual:
    print("El plazo fijo te deja más, te conviene!")
elif bonos_y_acciones > plazo_fijo_mensual:
    print("Los bonos te convienen!")
else:
    print("Te conviene el plazo de fijo Mensual")

