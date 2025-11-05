"""
Escribir un programa que lea una lista de números ingresados por el usuario separados por espacios y muestre cuántos números únicos hay en total. Utilizando Set

Ejemplo:

Entrada: 4 2 2 4 3 5 3
Salida: 4
"""
lista = input().split()

mi_set = set(lista)

print(len(mi_set))