"""
Solicitar dos cadenas e imprimir la cadena mas larga
"""
cadena_1 = input("Ingrese la cadena 1: ")
cadena_2 = input("Ingrese la cadena 2: ")

longitud_1 = len(cadena_1)
longitud_2 = len(cadena_2)

if longitud_1 > longitud_2:
    print(cadena_1)
elif longitud_2 > longitud_1:
    print(cadena_2)
else:
    print("Son iguales")