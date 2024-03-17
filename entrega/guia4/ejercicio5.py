# 5. Implementar una función que determine si dado un número este es par o impar.

def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

print(f"El número {4} es {par_impar(4)}")
