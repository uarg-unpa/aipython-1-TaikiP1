# 9. Crear una función que tome un string como parámetro y verifique si es un
# palíndromo. Ejemplo: Arenera, Narran. etc.

def esPalindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if palabra == palabra[::-1]:
        return "Si"
    else:
        return "No"

palabra = str(input("Ingrese una palabra para saber si es palindromo: "))
print(f'{palabra} es palindromo? {esPalindromo(palabra)}')

# print(f'La palabra Arenera, es palindromo? {esPalindromo("Arenera")}')
# print(f'La palabra Narran, es palindromo? {esPalindromo("Narran")}')
# print(f'La palabra Hola, es palindromo? {esPalindromo("Hola")}')
