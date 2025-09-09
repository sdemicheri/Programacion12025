#Simulacion de un Cajero Automatico

mi_Pin = "1234" #Pin que deberia ser el ingresado correctamente para poder usar las funciones del cajero
dinero = 10000 #Plata inicial que tiene en la cuenta bancaria

pin = input("Ingrese su pin de cuatro numeros: ") #Ingreso del pin que deberia ser el CORRECTO

if pin == mi_Pin:
    
    print("PIN ingresado correctamente...")

    print("---------------")
    print("CUENTA BANCARIA")
    print("---------------")
    print("Ingrese 1 para Ver sus Fondos")
    print("Ingrese 2 para Rretirar Fondos")
    print("Ingrese 3 para Ingresar Fondos")
    print("Ingrese 4 para Salir")

    opc = int(input("Ingrese la opcion que desea realizar: ")) #Ingreso de una de las opciones a realizar
    
    if opc == 1: #Valida si ingreso la opcion "1" y muestra el dinero disponible que tiene en la cuenta
        print("Sus fondos son de: $",dinero)
    
    elif opc == 2: #Valida si ingreso la opcion "2" y hace el ingreso del dinero que quiere retirar
    
        try:

            retirar = float(input("Ingrese la cantidad de dinero que quiere retirar: $"))

            if retirar <= 0 or retirar > dinero: #Valida si ingresa un monto que no tiene para retirar
                print("Ingreso un monto erroneo.")

            else:                                #Si ingreso un monto disponible para retirar, y lo retira
                retiro = dinero - retirar
                print("---------------------------------------------------")
                print("El dinero que le queda en su cuenta es de $",retiro)
                print("---------------------------------------------------")
                print("El monto que retiro es de: $",retirar)

        except Exception:
            print("Error al ingresar un monto NO VALIDO.")

    elif opc == 3:

        try:

            ing = float(input("Ingrese la cantidad de dinero que quier ingresar: $"))

            if ing <=0:     #Valida si el monto a ingresar es negativo, para no ingresar nada y tirar excepcion
                print("Ingrese un valor de dinero valido (tiene que ser positivo!!!!!)")

            else:
                dinero = dinero + ing #Valida si ingreso un monto valido a ingresar, y lo ingresa
                print("-------------------------------")
                print("Su saldo actual es de: $",dinero)
                print("-------------------------------")

        except Exception:
            print("Error al ingresar un monto NO VALIDO.")
    
    elif opc == 4:

        print("-------------------------------")
        print("Gracias por usar nuestros servicios...")
        print("-------------------------------")

    else: 
        print("Ingreso una opcion no valida...")

else:
    print("Ingreso un pin incorrecto...")
