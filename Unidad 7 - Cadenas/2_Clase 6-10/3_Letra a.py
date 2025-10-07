"""
Contar cuantas veces aparece la "a"
"""

cadena = "Hola a todos"
contador_a = 0
for i in range(len(cadena)):
    if cadena[i].lower() == 'a':
        print("Encontrada")