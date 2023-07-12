#ordeno las listas
def ordenar(alumnos, promedios):
    indices = []
    alumnos_ordenados = []
    promedios_ordenados = []
    alumnos_desordenados = []
    alumnos_desordenados = alumnos.copy()
    alumnos.sort()
    alumnos_ordenados = alumnos.copy()
    
    for i in range(len(alumnos_ordenados)):
        x = alumnos_desordenados.index(alumnos_ordenados[i])#recupero el index inicial del alumno con el nombre del alumno ordenado
        promedios_ordenados.append(promedios[x])#creo una lista ordenada de promedios con el valor del promedio encontrado en la lista desordenada
    return (alumnos_ordenados, promedios_ordenados)
    

def aprobados(alumnos, promedios, valor_minimo):
    aprobados = {}
    for i in range(len(alumnos)):
        if promedios[i] >= valor_minimo:
            aprobados["nombre"] = alumnos[i]
            aprobados["promedio"] = promedios[i]
            print (aprobados)
        i += 1

promedios = [8,5,3,7,6]
alumnos = ["andres", "ramiro", "jose", "mirta", "lucrecia"]
'''
para cargar las listas podría pedir por pantalla con un While hasta cambiar de lista o una cierta cantidad de alumnos
'''

#ordeno las listas
(alu, pro) = ordenar(alumnos, promedios)

#devuelvo un diccionario con los aprobados
aprobados(alu, pro, 6)

'''
salida cono diccionario para ver nombre y promedio escritos en vez de [andres, 8...]
{'nombre': 'andres', 'promedio': 8}
{'nombre': 'lucrecia', 'promedio': 6}
{'nombre': 'mirta', 'promedio': 7}  
'''