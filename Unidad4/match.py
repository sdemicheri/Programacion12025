try:
    numero = int(input("Ingrese un número del 1 al 5: "))
    match numero:
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
    if numero > 5:
        print("Ingreso un número no válido")
except ValueError:
    print("Ingreso un dato incorrecto")