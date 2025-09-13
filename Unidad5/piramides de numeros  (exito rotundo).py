filas = int(input("Ingrese la cantidad de filas: "))
for i in range(filas, 0, -1):
    for j in range(1, i + 1):  
        print(j, end=" ")
    print() 