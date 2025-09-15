"""

Utilizando la estructura repetitiva mientras. 
Realice un algoritmo permita el ingreso de números mientras no se ingrese un número negativo. 
Mostrar la cantidad de números ingresados al terminar
"""
contador = 0
numero = 0

while numero >= 0:
    try:
        numero = int(input("Ingrese un número: "))
        if numero >= 0:
            contador += 1
    except ValueError:
        print("Error en el ingreso de los datos, por favor ingrese un numero entero positivo")
print(f"Cantidad de números ingresados: {contador}")