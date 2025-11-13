"""
Generar un código que solicite al usuario un numero entero 
(se asume que el usuario ingresará siempre un entero, positivo y impar),
 y luego se dimensione una matriz nxn (donde n es el valor ingresado), 
 dicha matriz es inicializada en ceros y luego se le pide al usuario una opcion:

Identidad
Identidad inversa
Bordes laterales
Bordes superiores
Todos los bordes
Forma de suma (+)
Todas combinadas
Luego de que el usuario ingresa una opción se debe modificar el vector 
segun lo pedido por el usuario, y finalmente mostrarlo por pantalla. 
No se debe repetir la ejecución, una vez dibujado se termina el código.
"""
def dibujarDiagonalPrincipal(dimension,matriz):
    for i in range(dimension):
        matriz[i][i] = 1

def dibujarDiagonalSecundaria(dimension,matriz):
    fila = 0
    columna = (dimension - 1)
    for i in range(dimension):
        matriz[fila][columna] = 1
        fila += 1
        columna -= 1

def dibujarBordesLaterales(dimension,matriz):
    columna_inicial = 0
    columna_final = (dimension - 1)
    for i in range(dimension):
        matriz[i][columna_inicial] = 1
        matriz[i][columna_final] = 1

def dibujarBordesSuperiores(dimension,matriz):
    fila_inicial = 0
    fila_final = (dimension - 1)
    for i in range(dimension):
        matriz[fila_inicial][i] = 1
        matriz[fila_final][i] = 1

def dibujarSuma(dimension,matriz):
    centro = (dimension//2)
    for i in range(dimension):
        matriz[centro][i] = 1
        matriz[i][centro] = 1

try:
    n = int(input())
    columnas = n
    filas = n 
    matriz = [[0]*columnas for _ in range(filas)]
    opcion = int(input())

    if opcion == 1:
        dibujarDiagonalPrincipal(n,matriz)

    elif opcion == 2:
        dibujarDiagonalSecundaria(n,matriz)

    elif opcion == 3:
        dibujarBordesLaterales(n,matriz)
        
    elif opcion == 4:
        dibujarBordesSuperiores(n,matriz)
        
    elif opcion == 5:
        dibujarBordesLaterales(n,matriz)
        dibujarBordesSuperiores(n,matriz)
        
    elif opcion == 6:
        dibujarSuma(n,matriz)
        
    elif opcion == 7:
        dibujarDiagonalPrincipal(n,matriz)
        dibujarDiagonalSecundaria(n,matriz)
        dibujarBordesLaterales(n,matriz)
        dibujarBordesSuperiores(n,matriz)
        dibujarSuma(n,matriz)

    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j],end="")
        print()

except ValueError:
    print("ERROR: La entrada NO es valida, por favor ingrese un número entero")