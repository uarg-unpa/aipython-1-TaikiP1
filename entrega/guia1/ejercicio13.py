# 13. Escribir un programa que calcule el promedio de precios de 10 productos.

precios = []

for i in range(1, 11):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    precios.append(precio)

promedio = sum(precios) / len(precios)

print(f"El promedio de precios de los 10 productos es: {promedio}")