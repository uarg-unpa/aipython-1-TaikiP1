# 1. Iterar de 0 a 100 usando un bucle while y mostrar dichos números.

indice = 0

while indice <= 100:
    print(indice)
    indice += 1

# 2. Tomar el ejercicio 1 y realizarlo con un bucle for, tip usar range. los números deben
# salir uno al lado del otro.

for indice in range(101):
    print(indice, end=' ')  # Mostramos el número actual seguido de un espacio en lugar de una nueva línea