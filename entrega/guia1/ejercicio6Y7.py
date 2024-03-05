# 6. Crear un programa que solicite dos números enteros, luego realizar:
#   a. suma
#   b. resta
#   c. el producto
#   d. la potencia
#   e. el resto

primerNumeroInt = int(input("Ingrese el primer número entero: "))
segundoNumeroInt = int(input("Ingrese el segundo número entero: "))

sumaI = primerNumeroInt + segundoNumeroInt
restaI = primerNumeroInt - segundoNumeroInt
productoI = primerNumeroInt * segundoNumeroInt
potenciaI = primerNumeroInt ** segundoNumeroInt
restoI = primerNumeroInt / segundoNumeroInt

print(f"Suma: {sumaI}")
print(f"Resta: {restaI}")
print(f"Producto: {productoI}")
print(f"Potencia: {potenciaI}")
print(f"Resto: {restoI}")

# 7. Modificar el ejercicio 6 para que reciba un entero y un float.
primerNumeroFlotante = float(input("\nIngrese el primer número flotante: "))
segundoNumeroFlotante = float(input("Ingrese el segundo número flotante: "))

sumaF = primerNumeroFlotante + segundoNumeroFlotante
restaF = primerNumeroFlotante - segundoNumeroFlotante
productoF = primerNumeroFlotante * segundoNumeroFlotante
potenciaF = primerNumeroFlotante ** segundoNumeroFlotante
restoF = primerNumeroFlotante / segundoNumeroFlotante

print(f"Suma: {sumaF}")
print(f"Resta: {restaF}")
print(f"Producto: {productoF}")
print(f"Potencia: {potenciaF}")
print(f"Resto: {restoF}")

