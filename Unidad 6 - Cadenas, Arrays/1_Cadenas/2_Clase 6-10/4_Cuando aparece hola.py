"""
Encontrar la palabra hola
"""
cadena = "Hola a todos"

for i in  range(len(cadena)):
    if cadena[i:i+4].lower() == "hola":
        print("encontrada")