# 6. Crear una función que calcule el factorial de un número.
def factorial(num):
    if num == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado

print(f"El factorial de {5} es: {factorial(5)}")
