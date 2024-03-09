# 3. Solicite al usuario una contraseña, utilizando input(“Ingrese su contraseña”),
# almacene esta contraseña en una variable. Luego informar si la contraseña
# introducida coincide con la guardada sin tener en cuenta mayúsculas y
# minúsculas .

contrasenia_guardada = "CONtraseÑA123"
contrasenia_ingresada = str(input("Ingrese su contraseña: "))

if contrasenia_guardada == contrasenia_ingresada:
    print("¡La contraseña coinciden!")
else:
    print("La contraseña no coincide")

