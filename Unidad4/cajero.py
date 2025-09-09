try:
    try:
        clave = int(input("Ingrese la clave de cuatro dígitos: "))
        if clave < 0:
         print("La clave no puede ser negativa")
        elif clave <= 100 <= 999:
          print("La clave no tiene la cantidad de dígitos")
        elif clave > 9999:
            print("Error, la clave no puede tener más de cuatro dígitos")
        else:
            print("Clave aceptada")
            saldo = float(input("Ingrese el saldo de su cuenta "))
            print("Seleccione 1 para retirar dinero")
            print("Seleccione 2 para ver el saldo actual de la cuenta")
            print("Seleccione 3 para salir")
            opcion = int(input("Seleccione un número: "))
            if opcion == 1:
                dinero = float(input("Ingrese la cantidad de dinero a retirar: "))
                if dinero > saldo:
                    print("No tiene la cantidad suficiente para retirar ese monto")
                else:
                    saldo_final = saldo - dinero
                    print("El dinero se retiró exitosamente. Su saldo actual es: $", saldo_final)
            elif opcion == 2:
                print("El saldo actual de la cuenta es: $",saldo)
            elif opcion == 3:
                print("Gracias por utilizar nuestro servicio")
            else:
                print("Marcó una opción incorrecta")
    except ValueError:
        print("Ingreso un dato no válido")
except ValueError:
    print("Ingresó un dato no válido")
