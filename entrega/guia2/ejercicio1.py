# 1. Solicite información del usuario mediante el uso de input(“Ingrese su edad: ”). Si el
# usuario tiene 18 años o más, informar: tiene edad suficiente para conducir. Si tiene
# menos de 18 años,informe la cantidad de años que faltan.

edad = int(input("Ingrese su edad: "))

if edad < 18:
    años = (edad - 18) * -1
    print(f'Te faltan {años} para poder conducir')
else:
    print("Tiene edad suficiente para conducir")