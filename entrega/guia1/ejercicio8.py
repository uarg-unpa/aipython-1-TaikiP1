# 8. Se desea conocer el perímetro y el área de un rectángulo según su base y altura.
# Así mismo también se desean conocer los mismos datos para una circunferencia según su radio.

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
radio = float(input("Ingrese el radio: "))

perimetro = 2 * (base + altura)
area = base * altura
circunferencia = 3.14 * radio**2

print(f"El perímetro de un rectángulo es {perimetro} y su área es {area}")
print(f"La circunferencia es {circunferencia}")
