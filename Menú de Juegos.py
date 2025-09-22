jugando = True

while jugando:
    print("🎮 MENU DE JUEGOS 🎮")
    print("1) piedra ✊🏽, papel ✋🏽 o tijera ✌🏽")
    print("2) 🧐 Adivina el Numero 🧐")
    print("3) 🧠 Par o Impar 🧠")
    print("4) Salir...")
    
    opcion = int(input("Elige un juego: "))
    match opcion:
        case 1:
            print("piedra ✊🏽, papel ✋🏽 o tijera ✌🏽")
            print("1- Piedra \n2- Papel \n3- Tijera")
            print("Seleccione 0 si quiere salir.")
            nombre1 = input("Nombre jugador 1: ")
            nombre2 = input("Nombre jugador 2: ")
            while True:
                try:
                    jugador1 = int(input(f"{nombre1} elija su jugada (1, 2, 3): "))
                    jugador2 = int(input(f"{nombre2} elija su jugada (1, 2, 3): "))
                    if jugador1 == 0 or jugador2 == 0:
                        print("Saliste del juego 👋")
                        break
                    else:
                        if jugador1 == jugador2:
                            print("\n😐 𝗲𝗺𝗽𝗮𝘁𝗲 😐")
                        elif (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 == 3 and jugador2 == 2):
                            print(f"\n🥳 GANÓ {nombre1}🥳")
                        else:
                            print(f"\n🥳 GANÓ {nombre2} 🥳")
                except ValueError:
                    print("Ingrese los valores correctos.")
        case 2:
            print("\n🧐 Adivina el Numero 🧐")
            print("Ingresa un número del 1 al 10 (0 para salir)")
            numero = 6
            turno = 3
            while turno > 0:
                intento = int(input())
                if intento == 0:
                    break
                elif intento == numero:
                    print("\n🥳 CORRECTO! 🥳")
                    break
                else: 
                    intento != numero
                    turno -= 1 
                    print("\n 🥱 Incorrecto 🥱 \nIntente de nuevo")
        case 3:
            print("\n🧠 Par o Impar 🧠")
            numeroPoP = 9
            print("Escribe si es 'par' o 'impar' (0 para salir)")
            intentoPoP = input("Su respuesta: ").lower()
            while intentoPoP != 0:
                if intentoPoP == "0":
                    print("Saliste del juego 👋")
                    break
                if (numeroPoP % 2 == 0 and intentoPoP == "par") or (numeroPoP % 2 != 0 and intentoPoP == "impar"):
                    print("\n🥳 CORRECTO! 🥳")
                    break
                else:
                    print("\n🥱 Incorrecto 🥱 \nIntente de nuevo")
                    intentoPoP = input("Su respuesta: ").lower()
        case 4:
            print("\n🎮 Gracias por Jugar 🎮")
            jugando = False
