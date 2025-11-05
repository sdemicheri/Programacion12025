"""
Crear un programa que permita almacenar palabras en español y su traducción al inglés.
El programa debe permitir ingresar 3 pares de palabras, y luego pedir una palabra en español para mostrar su traducción.
Si la palabra no está registrada, debe mostrar el mensaje "Palabra no encontrada"

Ejemplo:

Entrada:
sol sun
luna moon
estrella star
cielo
Salida:
Palabra no encontrada
"""
try:
    diccionario = {}
    for i in range(3):
        cadena = input()
        espanol,ingles = cadena.split()
        diccionario[espanol]=ingles
    busqueda = input()
    print(diccionario[busqueda])
except KeyError:
    print("Palabra no encontrada")