# 14. Escribir una función que tome dos listas como parámetros y las intercale en una
# nueva, retornar la nueva lista resultante.

def listas(lista1, lista2):
    nueva_lista = []
    longitud_maxima = max(len(lista1), len(lista2))
    
    for i in range(longitud_maxima):
        if i < len(lista1):
            nueva_lista.append(lista1[i])
        if i < len(lista2):
            nueva_lista.append(lista2[i])
    
    return nueva_lista

listaA = ["Hola", "JUan", "Pepe"]
listaB = ["Chau", "Pablo", "Perez"]

print(f'Lista resultante: {listas(listaA, listaB)}')