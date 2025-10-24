try:    
    vector = [0] * 10
    contador = 0

    for i in range(10):
        vector[i] = int(input("Ingrese un numero: "))
        if vector[i] % 2 == 0:
            contador += 1

    print("Cantidad:",contador)
    print("Numeros:")
    
    for i in range(10):
        if vector[i] % 2 == 0:
            print(i)
except ValueError:
    print("ERROR")