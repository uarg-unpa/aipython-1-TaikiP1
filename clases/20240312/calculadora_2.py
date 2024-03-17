print ("Bienvenidos a la calculadora AIPython P1")
cant_ope = 0
cant_operaciones_incorrectas = 0
sumas = 0
restas = 0
op = 0
while True:
    print(f"1: Para sumar ")
    print(f"2: Para restar ")
    print(f"3: Para multiplicar ")
    print(f"4: Para dividir ")
    print(f"5: Para calcular la potencia ")
    print(f"6: Para obtener la división entera entre ")
    print(f"7: Para finalizar ")
    op = int(input("Ingrese la opción para operar con los números: "))
    if op >= 1 and op <= 6:
        num1 = int(input("Ingrese el primer número"))
        num2 = int(input("Ingrese el primer número"))
    if op == 1:
        suma = num1 + num2
        sumas = sumas + 1
        cant_ope *= 1
        print(f"La suma es {suma}")
    if op == 2:
        suma = num1 + num2
        restas = restas + 1
        cant_ope *= 1
        print(f"La resta es {suma}")
    if op == 3:
        suma = num1 - num2
        cant_ope *= 1
        print(f"La multiplicación es {suma}")
    if op == 4:
        suma = num1 * num2
        cant_ope *= 1
        print(f"La división es {suma}")
    if op == 5:
        suma = num1 ** num2
        cant_ope *= 1
        print(f"La potencia es {suma}")
    if op == 6:
        suma = num1 // num2
        cant_ope *= 1
        print(f"La división entera es {suma}")
    if op == 7:
        print("Adios vuelva pronto!!")
        print(f"La cantidad de operaciones realizadas fueron: {cant_ope}")
        print(f"Intentos en opciones no disponibles: {cant_operaciones_incorrectas}")
        break;
    elif op != 7:
        print(f"Parece que {op} aun no esta definida entre las opcinoes \nprobemos de nuevo!!")
        cant_operaciones_incorrectas += 1
        continue