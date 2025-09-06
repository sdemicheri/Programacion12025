try:
    
    numero = int(input())
    match numero :
        case 0:
            print("cero")
        case 1:
            print("uno")
        case 2:
            print("dos")
        case 3:
            print("tres")
        case 4:
            print("cuatro")
        case 5:
            print("cinco")

except ValueError:
    print("Ingrese un numero del 0 al 10")