"""

Utilizando la estructura repetitiva mientras. 
Realice un algoritmo permita el ingreso de números mientras no se ingrese un número negativo. 
Mostrar la cantidad de números ingresados al terminar
"""
contador = 0
numero = 0
while numero >= 0:
    numero = int(input("Ingrese un número: "))
    if numero >= 0:
        contador += 1
print(f"Cantidad de números ingresados: {contador}")