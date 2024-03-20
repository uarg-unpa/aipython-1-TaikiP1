# 7. Almacenar los nombres de tus compañías favoritas en una lista.
#   a. Recorrer la lista del ejercicio 7 y mostrar los datos con print.
#   b. Recorrer la lista del ejercicio 7 y mostrar el índice más el nombre de la compañía.
#   c. Modificar alguna/as de las compañía/s de la lista del ejercicio 7 y luego mostrar la lista.

companias = ["Meta", "Google", "Amazon", "Microsoft"]

print("a. Compañías favoritas: ")
for compania in companias:
    print(compania)

print("\nb. Índice y nombre de las compañías: ")
for indice, compania in enumerate(companias):
    print(f"{indice}: {compania}")

companias[0] = "Facebook"
companias[-1] = "Mercado libre"

print("\nc. Lista de compañías actualizada:")
for compania in companias:
    print(compania)
