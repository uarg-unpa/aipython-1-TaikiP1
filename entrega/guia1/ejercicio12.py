# 12. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantInvertir = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interés anual: "))
numAnios = int(input("Ingrese la cantidad de años a invertir: "))

total = cantInvertir * interesAnual * numAnios

print(f"Su capital es: {total}")