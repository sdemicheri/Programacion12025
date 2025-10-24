"""
Ingresar una frase y mostrar la palabra mas larga. 
Teniendo en cuenta que todas las palabras tienen distinta longitud.
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