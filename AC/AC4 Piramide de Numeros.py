numero = int(input("Ingrese un numero entero positivo: "))
try:
    for fila in range(numero, 0, -1):
        for numero in range(1, fila+1):
            print(numero, end=" ")
        print()
except ValueError:
    print("Ingrese los valores correctos.")