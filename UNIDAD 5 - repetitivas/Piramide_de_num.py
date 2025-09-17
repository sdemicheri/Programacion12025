# Pedir al usuario el número N
N = int(input("Ingresá un número entero positivo: "))

# Bucle desde N hasta 1 (en orden descendente)
for i in range(N, 0, -1):   # i empieza en N y termina en 1
    for j in range(1, i+1): # j va de 1 hasta i
        print(j, end=" ")   # imprime en la misma línea
    print()  # salto de línea después de cada fila