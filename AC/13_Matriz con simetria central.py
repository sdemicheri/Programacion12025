dimension = int(input())
matriz = [[0]*dimension for _ in range(dimension)]

for i in range(dimension):
    for j in range(dimension):
        matriz[i][j] = input()

k = 0
vector_auxiliar = [0]*(dimension*dimension)
for i in range(dimension-1,-1,-1):
    for j in range(dimension-1,-1,-1):
        vector_auxiliar[k] = matriz[i][j]
        k+=1

k = 0
matriz_invertida = [[0]*dimension for _ in range(dimension)]
for i in range(dimension):
    for j in range(dimension):
        matriz_invertida[i][j] = vector_auxiliar[k]
        k += 1

if matriz == matriz_invertida:
    print("Posse Simetria Central")
else:
    print("No Posse Simetria Central")  