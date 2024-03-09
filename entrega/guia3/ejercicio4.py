# 4. Escribir un programa que pida al usuario dos números enteros e imprima todos los
# números entre ellos.

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

if numero1 > numero2:
    for numero in range(numero2 + 1, numero1):
        print(numero, end=' ')
elif numero1 < numero2:
    for numero in range(numero1 + 1, numero2):
        print(numero, end=' ')
else:
    print("Los números son iguales")
