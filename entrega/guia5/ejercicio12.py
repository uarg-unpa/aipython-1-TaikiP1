# 12. Crear la siguiente lista
#       flores= [rosas, orquídea,lirio,tulipan, margarita, dalia, hortensia]
#   a. Mostrar tres elementos desde el tercer elemento.
#   b. Mostrar los elementos en posiciones pares desde la segunda posición
#   c. Mostrar todos los elementos desde la primera posición saltando de a tres elementos.

flores= ['rosas', 'orquídea', 'lirio', 'tulipan', 'margarita', 'dalia', 'hortensia']

print(f'a. Mostrar tres elementos desde el tercer elemento: {flores[2:5]}')

print(f'b. Mostrar los elementos en posiciones pares desde la segunda posición: {flores[1::2]}')

print(f'c. Mostrar todos los elementos desde la primera posición saltando de a tres elementos: {flores[::3]}')