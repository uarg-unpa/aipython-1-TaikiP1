# 15.Escribir un programa que pida un número entero e informe si dicho número es
# primo o no primo

# Números primos a probar
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97

numero = int(input("Ingrese un número entero: "))

es_primo = True

if numero >= 0:
    if numero <= 1:
        es_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
else:
    print("Ingrese un número natural")
