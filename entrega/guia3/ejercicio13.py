# 13.Construir un programa que lea un número natural N y calcule la suma de los
# primeros N números pares.

numero_natural = int(input("Ingrese un número natural: "))
suma = 0
contador = 0
numero = 2

if numero_natural >= 0:

    while contador < numero_natural:
        suma += numero
        numero += 2
        contador += 1

    print("La suma de los primeros", numero_natural, "números pares es:", suma)
else:
    print("Ingrese un número natural")
