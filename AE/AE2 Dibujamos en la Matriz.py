def imprimir():
     for i in range(dimension):
            for j in range(dimension):
                print(matriz[i][j], end="")
            print()  
def identidad():
    for i in range(dimension):
            for j in range(dimension):
                if matriz[i] == matriz[j]:
                    matriz[i][j] = 1
def identidadInversa():
    contadorF = 0
    contadorC = dimension-1
    for fila in range(0, dimension):
        matriz[contadorF][contadorC] = 1
        contadorF += 1
        contadorC -= 1
def bordesLaterales():
    for i in range(dimension):
        for j in range(dimension):
            matriz[i][dimension-1] = 1
            matriz[i][0] = 1
def bordesSuperiores():
    for i in range(dimension):
        for j in range(dimension):
            matriz[0][j] = 1
            matriz[dimension-1][j] = 1
def todosLosBordes():
    for i in range(dimension):
        for j in range(dimension):
            matriz[0][j] = 1
            matriz[dimension-1][j] = 1
            matriz[i][dimension-1] = 1
            matriz[i][0] = 1
def formaDeSuma():
    centro = dimension // 2
    for i in range(dimension):
        for j in range(dimension):
            matriz[centro][centro] = 1
            matriz[centro][j] = 1
            matriz[i][centro] = 1
dimension = int(input())
matriz = [[0]*dimension for i in range(dimension)]

opcion = int(input())

if opcion == 1:
    identidad()
    imprimir() 
if opcion == 2:
    identidadInversa()
    imprimir()
if opcion == 3:
    bordesLaterales()
    imprimir()
if opcion == 4:
    bordesSuperiores()
    imprimir()
if opcion == 5:
    todosLosBordes()
    imprimir()
if opcion == 6:
    formaDeSuma()
    imprimir()
if opcion == 7:
    identidad()
    identidadInversa()
    bordesLaterales()
    bordesSuperiores()
    todosLosBordes()
    formaDeSuma()
    imprimir()