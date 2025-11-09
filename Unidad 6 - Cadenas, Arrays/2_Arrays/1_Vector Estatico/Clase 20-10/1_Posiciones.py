try:    
    vector = [0] * 100
    posiciones = 0
    numero = int(input("Ingrese un nro o 0 para terminar: "))
    while numero != 0:
        vector[posiciones] = numero
        posiciones += 1
        numero = int(input("Ingrese un nro o 0 para terminar: "))
    print(vector)
    for i in range(posiciones):
        print(vector[i], end=" ")

except IndexError:
    print("No tenes mas espacio")
except ValueError:
    print("SOLO SE PERMITE NUMEROS")