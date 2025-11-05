"""
Imprimir las tablas de multiplicar en forma de matriz
"""
filas = 11
columnas = 11

matriz = [[0]*columnas for _ in range(filas)]

for f in range(filas):
    for c in range(filas):
        matriz [f][c] = f * c

for f in range(1,filas):
    for c in range(1,columnas):
        if (matriz[f][c] < 10):
            print(" "+ str(matriz[f][c]),end= " ")
        else:
            print(matriz[f][c],end= " ")
    print()