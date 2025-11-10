d = 6
matriz = [[0]*d for i in range(d)]

fila = 0
for i in range(d):
    matriz[fila][i] = 1
fila = d-1
for i in range(d):
    matriz[fila][i] = 1

columna = 0
for i in range(d):
    matriz[i][columna] = 1
columna = d-1
for i in range(d):
    matriz[i][columna] = 1

if d % 2 != 0:
    centro = d // 2
    matriz[centro][centro] = 2
elif d % 2 == 0:
    centro = d // 2
    matriz[centro-1][centro-1] = 2
    matriz[centro-1][centro] = 2
    matriz[centro][centro-1] = 2
    matriz[centro][centro] = 2

for i in range(d):
    for j in range(d):
        print(matriz[i][j],end=" ")
    print("")