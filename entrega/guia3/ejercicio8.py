# 8. Escribir un programa que pida un número entero positivo mayor a 3 y muestre
# por pantalla todos los números impares desde 1 hasta ese número.

numero = int(input("Ingrese un número entero positivo mayor a 3: "))

if numero >= 3:
    print(f"Números impares desde 1 hasta {numero}: ")
    for i in range(1, numero + 1, 2):
        print(i, end=" ")
    print("\n")
else:
    print("Número no válido, tiene que ser mayor a 3")