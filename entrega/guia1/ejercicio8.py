# 8. Se desea conocer el perímetro y el área de un rectángulo según su base y altura.
# Así mismo también se desean conocer los mismos datos para una circunferencia según su radio.

import math

base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
radio = int(input("Ingrese el radio: "))

print(f"El perímetro de un rectángulo es {2 * (base + altura)} y su área es {base * altura}")
print(f"La circunferencia es {math.pi * radio**2}")
