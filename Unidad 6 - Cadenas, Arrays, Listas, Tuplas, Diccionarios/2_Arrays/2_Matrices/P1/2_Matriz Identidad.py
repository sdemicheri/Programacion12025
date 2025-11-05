"Mostrar un msj si la matriz ingresada es o no matriz identidad"

n = int(input())
if n <= 12:
    filas = n
    columnas = n
    matriz = [[0]*columnas for _ in range(filas)] # DECLARAR LA DIMENSION DE LA MATRIZ Y PONER 0 COMO ELEMENTOS
    # PEDIR TODOS LOS ELEMENTOS DE LA MATRIZ Y AGREGARLOS
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = int(input())
    
    # COMPROBAR SI LA DIAGONAL PRINCIPAL TIENE 1
    contador_1 = 0
    for f in range(filas):
        for c in range(columnas):
            if f == c and matriz [f][c] == 1:
                contador_1 += 1
    
    # COMPROBAR SI EL RESTO DE ELEMENTOS SON 0
    contador_0 = 0
    for f in range(filas):
        for c in range(columnas):
            if f != c and matriz [f][c] == 0:
                contador_0 += 1

    # COMPROBAR AMBAS CONDICIONES PARA QUE SEA UNA MATRIZ IDENTIDAD
    if contador_1 == columnas and contador_0 == (filas*columnas)-(contador_1):
        print("Es Matriz Identidad")
    else:
        print("No es Matriz Identidad")