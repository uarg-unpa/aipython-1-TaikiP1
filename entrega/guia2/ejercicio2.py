# 2. Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?, 
#   para el ingreso de la edad use input(“Ingrese su edad: ”)
#   Use un condición anidada para:
#       Imprimir año si la diferencia es de 1, sino años para diferencias mayores.
#       Cuando las edades son iguales imprimir un mensaje personalizado, ser creativo!!

mi_edad = int(input("Ingrese su edad: "))
otra_edad = int(input("Ingrese mi edad: "))
diferencia_edades = abs(mi_edad - otra_edad)

if mi_edad > otra_edad:
    print("Eres mayor.")
elif mi_edad < otra_edad:
    print("Soy mayor")
else:
    print("¡Tenemos la misma edad!")


if diferencia_edades == 1:
    print("La diferencia de edad es de 1 año")
else:
    print(f"La diferencia de edad es: {diferencia_edades} años")
