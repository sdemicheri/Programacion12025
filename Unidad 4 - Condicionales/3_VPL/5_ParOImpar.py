"""
Utilizando la estructura condicional doble. Realice un algoritmo que ingresando un número, 
muestre un mensaje indicando si el número es par o es impar.

Entrada: un número.

Salida: "Es par" o "Es impar".
"""

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")