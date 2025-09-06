try:

    numero = int(input("Ingrese numero entero de tres cifras: "))
    if numero < 0:
        print("El numero debe ser mayor a 0")
    elif numero < 100 or numero > 999:
        print("El numero debe ser de 3 cifras")
    
    else:
        primeraUnidad = numero // 100
        ultimaUnidad = numero % 10
        if primeraUnidad == ultimaUnidad:
            print("Es capicua")
        else:
            print("No es capicua")

except ValueError:
    print("Error al ingresar los datos")