"""
Determinar la cantidad de palindromos dentro de una frase.

Un palindromo es una palabra que puede leerse tanto al derecho como al reves.

La busqueda no debe ser sensible a las mayusculas y minusculas.
"""
cadena = input("Ingrese una oracion: ").lower()                
palabra = ""
palabra_invertida = ""
posicion_espacio = 0
contar_palindroma = 0
contar_espacios = 0

for i in range(len(cadena)):

    primer_espacio = posicion_espacio

    if cadena[i] == " ":
        contar_espacios += 1
        posicion_espacio = i

        if contar_espacios == 1:
            for i in range(primer_espacio,posicion_espacio,1):
                if cadena[i] != "," and cadena[i] != ":" and cadena[i] != ".":
                    palabra += cadena[i]
            for i in range(posicion_espacio-1,primer_espacio-1,-1):
                if cadena[i] != "," and cadena[i] != ":" and cadena[i] != ".":                
                    palabra_invertida += cadena[i]
            if palabra == palabra_invertida and len(palabra) > 2:
                contar_palindroma += 1
            else:
                palabra = ""
                palabra_invertida = ""

        elif contar_espacios > 1:
            for i in range(primer_espacio+1,posicion_espacio,1):
                if cadena[i] != "," and cadena[i] != ":" and cadena[i] != ".":                
                    palabra += cadena[i]
            for i in range(posicion_espacio-1,primer_espacio,-1):
                if cadena[i] != "," and cadena[i] != ":" and cadena[i] != ".":                
                    palabra_invertida += cadena[i]
            if palabra == palabra_invertida and len(palabra) > 2:
                contar_palindroma += 1

        palabra = ""
        palabra_invertida = ""

print("Cantidad de palabras palindroma: ",contar_palindroma)   