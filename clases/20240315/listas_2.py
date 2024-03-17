# Creación de listas usando el metodo
# nombres=list()
# Crear una lista con valores iniciales
nombres=list(['Gaston', 'Eva', 'Lautaro'])
print(nombres)
# metodos, append, permite agregar un elemento al final de la lista
# nombres.append('Sandra')
# print(nombres)
# insert

# Vamos a utilizar la función id
print(id(nombres))

# nombres.insert(0, 'Victoria')
# print(nombres)
# Utilizar el operador in
# for nombre in nombres:
#     print(nombre)
# mutabilidad
nombres[4]='Lorenza'
for nombre in nombres:
    print(nombre)

print(id(nombres))