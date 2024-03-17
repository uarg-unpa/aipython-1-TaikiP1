# 4. Escribir una función que tome un número como entrada e imprima la tabla de
# multiplicar del 1 al 10, con el siguiente formato.

# 4 x 1 = 4
# ............
# ............

def tabla_multiplicar(num):
    for i in range(11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
        print("." * 14)

tabla_multiplicar(4)
