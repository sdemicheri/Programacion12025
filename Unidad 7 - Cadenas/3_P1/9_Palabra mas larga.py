"""
Ingresar una frase y mostrar la palabra mas larga. 
En caso de que existan dos palabras o mas que tengan el mismo largo, 
que la más larga, sin importar si son repetidas, 
mostrarlas en el orden en el que aparecen en el texto.

Ejemplo 1:
Entrada:
Hola Mundo
Salida:
Mundo

Ejemplo 2:
Entrada:
Hola todo bien por aca amor
Salida:
Hola
todo
bien
amor
"""
frase = input()
letra = ""
palabra_actual = ""
palabra_mas_larga = ""
longitud_maxima = 0

for i in range(len(frase)):
    letra = frase[i]
    if letra != " ":
        palabra_actual += letra
    else:
        if len(palabra_actual) > longitud_maxima:
            palabra_mas_larga = palabra_actual
            longitud_maxima = len(palabra_actual)
        palabra_actual = ""

if len(palabra_actual) > longitud_maxima:
    palabra_mas_larga = palabra_actual

print(palabra_mas_larga)