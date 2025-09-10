try:

    nota = int(input("Ingrese la calificacón: "))
    match nota:
        case 1:
            print("Uno")
        case 2:
            print("Dos")
        case 3:
            print("tres")
        case 4:
            print("Cuatro")
        case 5:
            print("Cinco")
        case 6:
            print("Seis")
        case 7:
            print("Siete")
        case 8:
            print("Ocho")
        case 9:
            print("Nueve")
        case 10:
            print("Diez")

    if nota < 6:
        print("Desaprobado")
    elif nota >= 6:
        print("Aprobado")
    elif nota >= 8:
        print("Promoción directa")
    elif nota == 10:
        print("Calificación Perfecta")

except ValueError:
    print("Ingrese los valores correctos.")