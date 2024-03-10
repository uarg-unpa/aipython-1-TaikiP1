# 14.Escribir un programa que recibe como entrada desde el usuario dos números
# enteros e imprimir todos los números pares entre ellos.

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))


if numero1 >= 0 and numero2 >= 0:
    if numero1 == numero2:
        print("Los números ingresados son iguales")
    else:
        print("Números pares entre", numero1, "y", numero2, ":")
        for num in range(numero1 + 1, numero2 + 1):
            if num % 2 == 0:
                print(num)
else:
    print("Ingrese un número natural")
