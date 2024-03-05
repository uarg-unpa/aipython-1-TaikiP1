# 5. Utilizando la función input
#   a. Crear un programa que imprima un mensaje (usar función print) solicitando,
#       el nombre, el apellido y la edad desde la terminal y luego darle un mensaje
#       ,“ser creativo”, utilizando los tres datos ingresados.
#   b. Modificar el ejercicio anterior para no utilizar la función print para mostrar el
#       mensaje al solicitar los datos. Tip pasarle el argumento a la función input.

# a
nombre = str(input("Ingresar su nombre: "))
apellido = str(input("Ingresar su apellido: "))
edad = int(input("Ingresar su edad: "))

print(f"El nombre ingresado es {nombre}, " + f"el apellido es {apellido} y " + f"su edad es {edad}")

# b

resultado = f"El nombre ingresado es {nombre}, " + f"el apellido es {apellido} y " + f"su edad es {edad}"
input(resultado)