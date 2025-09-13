N = int(input("ingrese un numero:"))
numeros = 0
while (N > numeros):
    numeros += 1
    if( N % numeros != 0):
        print("es un numero primo")
        break
    else:
        print("no es un numero primo")
        break