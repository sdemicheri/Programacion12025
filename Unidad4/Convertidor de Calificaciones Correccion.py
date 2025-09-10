try:

    nota = float(input("Ingrese la calificacón: "))
    entero = nota // 1
    decimal = (nota * 10) % 10
    match entero:
        case 1:
            print("Uno", end=" ")
        case 2:
            print("Dos", end=" ")
        case 3:
            print("tres", end=" ")
        case 4:
            print("Cuatro", end=" ")
        case 5:
            print("Cinco", end=" ")
        case 6:
            print("Seis", end=" ")
        case 7:
            print("Siete", end=" ")
        case 8:
            print("Ocho", end=" ")
        case 9:
            print("Nueve", end=" ")
        case 10:
            print("Diez", end=" ")

    print("coma", end=" ")

    match decimal:
            case 1:
                print("uno", end=" ")
            case 2:
                print("dos", end=" ")
            case 3:
                print("tres", end=" ")
            case 4:
                print("cuatro", end=" ")
            case 5:
                print("cinco", end=" ")
            case 6:
                print("seis", end=" ")
            case 7:
                print("siete", end=" ")
            case 8:
                print("ocho", end=" ")
            case 9:
                print("nueve", end=" ")
            case 10:
                print("diez", end=" ")

except ValueError:
    print("Ingrese los valores correctos.")