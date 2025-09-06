try:
    numero = int(input())
    if numero == 0:
        print("cero")
    elif numero == 1:
        print("uno")
    elif numero == 2:
        print("dos")
    elif numero == 3:
        print("tres")
    elif numero == 4:
        print("cuatro")
    elif numero == 5:
        print("cinco")
except ValueError:
    print("Ingrese un numero del 0 al 5: ")