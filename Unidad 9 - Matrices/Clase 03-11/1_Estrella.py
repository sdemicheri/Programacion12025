"""
Imprimir una matriz que tenga forma de estrella
"""
filas = 5
columnas = 5
matriz = [[""]*columnas for _ in range(filas)]

# DIAGONAL PRINCIPAL
for f in range(5):
    for c in range(5):
        if f == c:
            matriz[f][c] = "+"

# DIAGONAL SECUNDARIA
ultimo = columnas - 1
for i in range(5):
    matriz[i][ultimo] = "+"
    ultimo -= 1

# NUMEROS DEL MEDIO
centro = filas // 2

for i in range(5):
    matriz[centro][i] = "+"

for i in range(5):
    matriz[i][centro] = "+"

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c],end=" ")
    print()