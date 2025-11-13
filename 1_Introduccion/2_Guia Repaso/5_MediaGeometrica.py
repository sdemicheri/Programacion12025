"""
Escriba un algoritmo que halle la media geométrica de tres valores X, Y, Z. Este debe emitir
los tres valores por separado y luego el valor medio. La media geométrica es igual a (X*Y*Z)**(1/3)
"""
X = float(input("Ingrese el valor de X: "))
Y = float(input("Ingrese el valor de Y: "))
Z = float(input("Ingrese el valor de Z: "))

media_geométrica = (X * Y * Z)**(1/3)

print("Los valores ingresados son:")
print("X:", X)
print("Y:", Y)
print("Z:", Z)
print("La media geométrica es:", media_geométrica)