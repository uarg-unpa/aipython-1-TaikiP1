# 15. Implementar una función que tome una lista de números y retorna el promedio de
# sus elementos.

def calcPromedio(numeros):
    promedio = 0
    suma = 0
    cant = 0
    for i in range(len(numeros)):
        suma += numeros[i]
        cant += 1
    
    promedio = float(suma//cant)
    return promedio

numeros = [1, 10, 20, 4, 30]
print(f'El promedio de los siguientes números {numeros} es: {calcPromedio(numeros)}')