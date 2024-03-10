# 12. Escribir un programa que pida un número natural N al usuario e imprima por
# pantalla la suma de los números naturales de 1 hasta N.
# Por ejemplo para N = 5, la salida debe ser:
# 1 + 2 + 3 + 4 + 5 = 15

numero_natural = int(input("Ingrese un número natural: "))
suma = 0
for i in range(1, numero_natural + 1):
    suma += i
    if i != numero_natural:
        print(i, "+", end=" ")
    else:
        print(i, "=", suma)