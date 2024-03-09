# 4. Obtenga dos números del usuario mediante input. Si a es mayor que b, devuelve a
# es mayor que b, si a es menor que b, devuelve a es menor que b de lo contrario, a
# es igual a b.

numero_a = float(input("Ingrese el primer número: "))
numero_b = float(input("Ingrese el segundo número: "))

# Comparamos números
if numero_a > numero_b:
    print("a es mayor que b")
elif numero_a < numero_b:
    print("a es menor que b")
else:
    print("a es igual a b")
