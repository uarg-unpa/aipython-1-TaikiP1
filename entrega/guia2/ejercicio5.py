# 5. Escriba un programa que pida al usuario un número entero e indique si es par o impar.

numero = int(input("Ingrese un número entero: "))

# El número es par o impar?
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
