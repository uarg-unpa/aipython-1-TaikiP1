# 4. Crear una lista de tus frutas favoritas.
#   a. Imprimir la longitud.
#   b. Eliminar el primer elemento de la lista.
#   c. Agregar un elemento al final de la lista.
#   d. Imprimir los resultados anteriores.

# Crear una lista de frutas favoritas
frutas = ["manzana", "banana", "mango", "naranja"]

print(f'a. La longitud de las frutas es: {len(frutas)}')

eliminarFruta = frutas.pop(0)
print(f'b. Se elimino la primera fruta: {eliminarFruta}')

frutas.append("sandia")
print(f'c. Se agrego una nueva fruta: {frutas}')

print(f'd. Lista de las frutas: {frutas}')
