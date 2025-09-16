"""
Escribir un programa que, dado un número entero positivo N, 
imprima una pirámide de números invertida donde:

Por ejemplo, si N=5, la salida debería ser:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
nro = int(input("Ingrese un número entero positivo: ")) 
while nro > 0:
    for i in range(1,nro+1): #  itera desde la variable 1 hasta el nro+1
        print(i,end= ' ')    #  mientras itera con paso 1 imprime esa posición del nro
    nro -= 1                 #  al nro le resto 1 para que cada vez se vaya imprimiendo menos cantidad
    if nro >= 1:             #  por cada impresión de la fila hago un salto de linea,
        print()              #  excepto cuando solo queda el 1             