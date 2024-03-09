# 22. Cortar las dos primeras palabras de la frase ‘’El razonamiento matemático puede
# considerarse más bien esquemáticamente como el ejercicio de una combinación de
# dos instalaciones, que podemos llamar la intuición y el ingenio”.

palabra = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"

print(palabra[0:15])

# 24. Usar el carácter de escape y nueva línea para separar la frase del ejercicio 22 en dos líneas.

print(f'{palabra[0:54]}', f'{palabra[55:]}', sep="\n")