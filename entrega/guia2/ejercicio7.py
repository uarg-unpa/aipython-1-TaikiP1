# 7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
#    ● 80-100, A
#    ● 70-89, B
#    ● 60-69, C
#    ● 50-59, D
#    ● 0-49, F

puntuacion = int(input("Ingrese la puntuación del estudiante: "))

# Clasificamos la puntuación
if puntuacion >= 80 and puntuacion <= 100:
    print("La puntuación corresponde a la clasificación A.")
elif puntuacion >= 70 and puntuacion <= 89:
    print("La puntuación corresponde a la clasificación B.")
elif puntuacion >= 60 and puntuacion <= 69:
    print("La puntuación corresponde a la clasificación C.")
elif puntuacion >= 50 and puntuacion <= 59:
    print("La puntuación corresponde a la clasificación D.")
elif puntuacion >= 0 and puntuacion <= 49:
    print("La puntuación corresponde a la clasificación F.")
else:
    print("La puntuación ingresada no es válida.")
