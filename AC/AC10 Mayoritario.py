try:
    vectorA = [0]*10
    auxiliar = vectorA[0]
    mayoritario = 0
    numeroN = int(input())
    vector = input().split()
    
    for i in range(numeroN):
        vectorA[int(vector[i])] += 1
    for i in range(len(vectorA)):
        if vectorA[i] > auxiliar:
            auxiliar = vectorA[i]
            mayoritario = i    
    if auxiliar > len(vector) // 2:
        print(mayoritario)
    else:
        print("No hay mayoritario")

except ValueError:
    print("Ingrese un valor")