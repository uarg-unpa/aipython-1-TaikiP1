# 11. Escribir un programa que pida al usuario un número entero y muestre por
# pantalla un triángulo rectángulo como el que se muestra
# Si se ingresa el número 9, el resultado será
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()