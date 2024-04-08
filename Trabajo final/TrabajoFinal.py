import random

def lanzarDado(caras):
    return random.randint(1, caras)

def lanzamientos(dados, caras, cantidad):
    resultados = []
    for _ in range(cantidad):
        lanzamientos = [lanzarDado(caras) for _ in range(dados)]
        resultados.append(lanzamientos)
    return resultados

def mostrarResultados(resultados):
    print("\nResultados individuales:")
    for i, lanzamiento in enumerate(resultados, 1):
        print(f"Lanzamiento {i}: {lanzamiento}, Total: {sum(lanzamiento)}")

def mostrarEstadisticas(resultados):
    sumMinima = min(sum(resultado) for resultado in resultados)
    sumMaxima = max(sum(resultado) for resultado in resultados)
    sumPromedio = sum(sum(resultado) for resultado in resultados) / len(resultados)
    print("\nEstadísticas:")
    print(f"Total de lanzamientos: {len(resultados)}")
    print(f"Suma mínima: {sumMinima}")
    print(f"Suma máxima: {sumMaxima}")
    print(f"Suma promedio: {sumPromedio}")

def main():
    print("Bienvenido al simulador de lanzamientos de dados")
    resultados = None
    while True:
        print("\n¿Qué acción deseas realizar?")
        print("1. Realizar lanzamientos")
        print("2. Ver resultados")
        print("3. Ver estadísticas")
        print("4. Salir")
        opcion = input("Ingrese el número correspondiente a la acción: ")
        
        if opcion == "1":
            dados = int(input("Ingrese la cantidad de dados a lanzar: "))
            caras = int(input("Ingrese el número de caras de cada dado: "))
            cantidad = int(input("Ingrese la cantidad de lanzamientos a realizar: "))
            resultados = lanzamientos(dados, caras, cantidad)
            print("Lanzamientos realizados.")
        elif opcion == "2":
            if resultados:
                mostrarResultados(resultados)
            else:
                print("Aún no se han realizado lanzamientos.")
        elif opcion == "3":
            if resultados:
                mostrarEstadisticas(resultados)
            else:
                print("Aún no se han realizado lanzamientos.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

main()
