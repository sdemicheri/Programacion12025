lados = 11
matriz = [[0]*lados for i in range(lados)]

for i in range(lados):
    for j in range(lados):
        if lados % 2 != 0:
            centro = lados // 2
            matriz[centro][j] = "*"
            matriz[i][i] = "*"

paraAtras = lados -1
for i in range(lados):              
        matriz[i][paraAtras] = "*"
        paraAtras -= 1

for i in range(lados):
    for j in range(lados):
        print(matriz[i][j],end=" ")
    print("")