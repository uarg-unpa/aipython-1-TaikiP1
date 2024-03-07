# 10. Escribir un programa que pida una temperatura en grados Celsius al usuario, realice
# la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

gradosF = (temperatura * 9/5) + 32

print(f"Esta haciendo {gradosF} grados Fahrenheit")