"""
Leer un arreglo de tamaño N (1 ≤ N ≤ 100) de enteros. Determinar si existe un “elemento mayoritario” que aparezca más de ⌊N/2⌋ veces. Si existe, mostrar ese valor; si no, mostrar “No hay mayoritario”.

Entradas:

Un entero N.

N enteros.

Salida:

Un único valor entero (el elemento mayoritario) o el texto  No hay mayoritario.

Ejemplo

Entrada: 7
2 5 2 2 3 2 4
Salida: 2
Explicación: 2 aparece 4 veces, que es mayor que 7/2.

"""
n = int(input())
vector = input().split()

contador = 0
maxima_long = 0

for i in range(n):
    auxiliar = vector[i]

    for j in range(n):
        if auxiliar == vector[j]:
            contador += 1
    if contador > maxima_long:
        mayoritario = auxiliar
        maxima_long = contador

    contador = 0

if maxima_long > len(vector) // 2:
    print(mayoritario)
else:
    print("No hay mayoritario")