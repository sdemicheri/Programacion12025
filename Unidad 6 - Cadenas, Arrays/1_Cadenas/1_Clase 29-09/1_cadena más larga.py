"""
Pedir 2 cadenas e imprimir la cadena mas larga
"""
cadena_1 = input("Ingrese la cadena 1: ")
cadena_2 = input("Ingrese la cadena 2: ")

if len(cadena_1) > len(cadena_2):
    print(cadena_1)
elif len(cadena_2) > len(cadena_1):
    print(cadena_2)
else:
    print("Son iguales en longitud")