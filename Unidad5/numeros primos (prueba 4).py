numero = int(input("ingrese un numero:"))
numeros = 0
while (numero > numeros):
    numeros += 1
    if( numero % numeros == 0):
        print("su numero es primo")
    else:
        print(" su numero no primo")
        break