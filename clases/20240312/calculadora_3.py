def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def producto(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return a**b

def div_entera(a,b):
    return a//b

def mostrar_menu():
    print(f"1: Para sumar ")
    print(f"2: Para restar ")
    print(f"3: Para multiplicar ")
    print(f"4: Para dividir ")
    print(f"5: Para calcular la potencia ")
    print(f"6: Para obtener la división entera entre ")
    print(f"7: Para finalizar ")

# def mostrar_estadistica(sumas, restas, cant_operaciones, cant_operaciones_incorrectas):
    #mostrar esta estadistica utilizando tabulacion y que se imprima como una tabla
    #que tenga titulos y la informacion
    # pass

def mostrar_estadistica(datos):
    for dato in datos:
        print(dato)

def main():
    print ("Bienvenidos a la calculadora AIPython P1")
    cant_ope = 0
    cant_operaciones_incorrectas = 0
    sumas = 0
    restas = 0
    op = 0

    print(f"1: Para sumar ")
    print(f"2: Para restar ")
    print(f"3: Para multiplicar ")
    print(f"4: Para dividir ")
    print(f"5: Para calcular la potencia ")
    print(f"6: Para obtener la división entera entre ")
    print(f"7: Para finalizar ")



main()