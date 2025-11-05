"""
Ingresar una matriz de 3x3 y determinar la cantidad 
de elementos mayores al promedio.
"""
filas = 3
columnas = 3

matriz = [[0]*columnas for _ in range(filas)]

suma = 0

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input())
        suma += matriz[f][c]

promedio = suma / 9     
for f in range(filas):
    for c in range(columnas):
        if matriz[f][c] > promedio:
            contador += 1

print(contador)