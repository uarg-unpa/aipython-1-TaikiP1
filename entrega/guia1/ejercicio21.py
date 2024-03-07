# 21. Escribir un programa que pida una palabra al usuario y reemplace todas las letras
# "a" por 😃 y muestre el resultado por pantalla.

palabra = str(input("Ingrese una palabra: "))

palabraReemplazada = palabra.replace("a", "😃")

print(f'{palabraReemplazada}')