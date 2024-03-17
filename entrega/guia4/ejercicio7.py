# 7. Escribir una función que tome tres números como entrada y retorna el máximo.

def maximo(num1, num2, num3):
    return max(num1, num2, num3)

num1 = -10
num2 = -3
num3 = -8
resultado = maximo(num1, num2, num3)
print(f"El máximo de los números {num1}, {num2} y {num3} es: {resultado}")
