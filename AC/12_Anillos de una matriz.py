filas = int(input())
columnas = int(input())
matriz = [[0]*columnas for _ in range(filas)]
for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input())

fila_inicial = 0
fila_final = filas - 1
columna_inicial = 0
columna_final = columnas - 1

while (fila_inicial <= fila_final) and (columna_inicial <= columna_final):
    anillosSuma = 0
    # primer fila
    for i in range(columna_inicial,columna_final+1):
        anillosSuma += matriz[fila_inicial][i]

    # ultima fila
    for i in range(columna_inicial,columna_final+1):
        anillosSuma += matriz[fila_final][i]

    # primer columna
    for i in range(fila_inicial+1,fila_final):
        anillosSuma += matriz[i][columna_inicial]

    # ultima columna
    for i in range(fila_inicial+1,fila_final):
        anillosSuma += matriz[i][columna_final]

    fila_inicial += 1
    fila_final -= 1
    columna_inicial += 1
    columna_final -= 1

    print(anillosSuma)