"""
Ingresar una frase y mostrar la palabra mas larga. 
En caso de que existan dos palabras o mas que tengan el mismo largo, 
que la más larga, sin importar si son repetidas, 
mostrarlas en el orden en el que aparecen en el texto.
"""

cadena = "Solos en el bosque de neuquen encontramos un oso."
# salida: encontramos

palabra = ""
contador_letras = 0
for i in range(len(cadena)):
    if cadena[i] == " ":
        palabra += cadena[i]
        contador_letras += 1

palabra_mas_larga = palabra
print(palabra)