dimension = int(input())
valores = []
total = dimension * dimension

for i in range(total):
    try:
        elementos = input()
    except EOFError:
        elementos = ""
    valores = valores + [elementos]
    
while len(valores) > dimension * dimension:
    valores.pop()   # saca el último elemento
while len(valores) < dimension * dimension:
    valores = valores + ["-"]

matriz = [[0] * dimension for i in range(dimension)]

posicion = 0
for i in range(dimension):
    for j in range(dimension):
        matriz[i][j] = valores[posicion]
        posicion += 1
simetrica = False
for i in range(dimension):
    for j in range(dimension):
        if matriz[i][j] == matriz[dimension - 1 - i][dimension - 1 - j]:
            simetrica = True

if simetrica:
    print("Posse Simetria Central")
else:
    print("No Posse Simetria Central")