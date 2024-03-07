# 11. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.

horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
costo = int(input("Ingrese el costo por horas: "))

sueldo = horasTrabajadas * costo

print(f"Su sueldo es: {sueldo}")