# 13. Escribir una función que dada una lista de caracteres cuente la cantidad de vocales
# y retorne esa información.

def lista(caracteres):
    voc = 0
    for c in caracteres:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return voc

print(f'Lista de caracteres: {lista("murcielago")}')