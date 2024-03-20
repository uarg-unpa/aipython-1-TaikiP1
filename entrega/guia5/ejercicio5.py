# 5. Dada una lista mostrar el primer elemento, el del medio y el último.

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

primerElemento = lista[0]
ultimoElemento = lista[-1]

longitud = len(lista)
if longitud % 2 == 0:
    indice = longitud // 2 - 1
else:
    indice = longitud // 2

medio = lista[indice]

print(f'Primer elemento: {primerElemento}')     # Resultado del print: a
print(f'Elemento del medio: {medio}')           # Resultado del print: e
print(f'Último elemento: {ultimoElemento}')     # Resultado del print: i