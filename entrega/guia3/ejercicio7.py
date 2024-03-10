# 7. Escribir un programa que pregunte el nombre de usuario y un número entero
# e imprima en diferentes líneas el nombre de usuario tantas veces como el
# número introducido.

nombre = input("Ingrese su nombre de usuario: ")
numero = int(input("Ingrese un número entero: "))

for _ in range(numero):
    print(nombre)