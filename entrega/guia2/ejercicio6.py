# 6. Escriba un programa que pida al usuario un número entero del 1 al 7 y muestre por
# pantalla a qué día de la semana corresponde. Controlar que el número se encuentre
# dentro del rango [1-7], sino es así, mostrar un mensaje.
# Por ejemplo, si se ingresa el número 2 la salida debe ser martes.

numero = int(input("Ingrese un número entero del 1 al 7: "))

# Verificamos si el número está dentro del rango válido [1-7]
if numero > 0 and numero < 8:
    semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dia = semana[numero - 1]
    print(f"El número {numero} corresponde al {dia}.")
else:
    print("El número ingresado no está dentro del rango [1-7].")
