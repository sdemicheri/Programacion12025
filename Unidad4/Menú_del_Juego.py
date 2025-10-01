opcion = -1  #Se usa opcion = -1 para iniciar el bucle.

while opcion != 0:     #El while mantiene el programa activo hasta que el usuario elige 0 para salir.
    print("="*18)
    print("MENÚ DE JUEGO")   #Dentro del bucle se muestra el menú y se ejecuta el juego correspondiente.
    print("="*18)
    print("")
    print("1. PIEDRA, PAPEL O TIJERA ")
    print("2. PREGUNTADO")
    print("3. TRUCO")
    print("0. Salir del programa")
    print("")
    elige_una_opcion = input("Elige un juego del 1 al 3 ")
    print("")
    print("-"*60)
    opcion = int(elige_una_opcion)
    
    if opcion == 1: #Si opcion fue igul a 1, jugas PIEDRA, PAPELO TIJERA.
        turnos = 3   #Cantidades de ronda a jugar.
        ronda = 1    #Contador de la ronda actual.
        puntos_jugador1 = 0 #Aumulador de los resultados.
        puntos_jugador2 = 0 #Aumulador de los resultados.
        empates = 0
    

        print("Ingrese nombre/apodo del Jugador 1:")
        nombre1 = input()                                #Se pide el nombre de cada jugador.
        print("Ingrese nombre/apodo del Jugador 2:")
        nombre2 = input()

        while ronda <= turnos:
            print("")
            print("Ronda", ronda)
            print("1 = Piedra")
            print("2 = Papel")
            print("3 = Tijera")

            print(nombre1, "elige tu opción (1, 2 o 3):")
            jugada1 = int(input())
            if jugada1 == 1:
                print("Piedra")
            elif jugada1 == 2:
                print("Papel")
            elif jugada1 == 3:
                print("Tijera")
            else:
                print("ERROR, OPCIÓN INVÁLIDA")

            print(nombre2, "elige tu opción (1, 2 o 3):")
            jugada2 = int(input())
            if jugada2 == 1:
                print("Piedra")
            elif jugada2 == 2:
                print("Papel")
            elif jugada2 == 3:
                print("Tijera")
            else:
                print("ERROR, OPCIÓN INVÁLIDA")

            if jugada1 == jugada2:
                print("¡EMPATE!")
                empates += 1
            elif (jugada1 == 1 and jugada2 == 3) or (jugada1 == 2 and jugada2 == 1) or (jugada1 == 3 and jugada2 == 2):
                print("GANA", nombre1)
                puntos_jugador1 = puntos_jugador1 + 1
            elif (jugada2 == 1 and jugada1 == 3) or (jugada2 == 2 and jugada1 == 1) or (jugada2 == 3 and jugada1 == 2):
                print("GANA", nombre2)
                puntos_jugador2 += 1
            else:
                print("No se puede jugar con esas opciones.")

            ronda += 1

        print("")
        print("=== RESULTADO FINAL ===")
        print(nombre1, "ganó", puntos_jugador1, "ronda(s)")  #Se muestra el resumen de puntos acumulados.
        print(nombre2, "ganó", puntos_jugador2, "ronda(s)")  
        print("Empates:", empates)

        if puntos_jugador1 > puntos_jugador2:                #Se declara el ganador según quién tiene más rondas ganadas.
            print("🏆 ¡Ganador:", nombre1, "!")
        elif puntos_jugador2 > puntos_jugador1:
            print("🏆 ¡Ganador:", nombre2, "!")
        else:
            print("¡El juego terminó en empate total!")

        print("Presiona ENTER para volver al menú.")
        input()

    elif opcion == 2:
        print("Juego PREGUNTADO aún no disponible.")
        print("Presiona ENTER para volver al menú.")
        input()

    elif opcion == 3:
        print("Juego TRUCO aún no disponible.")
        print("Presiona ENTER para volver al menú.")
        input()

    elif opcion == 0:
        print("¡Gracias por jugar! 👋")

    else:
        print("Opción inválida. Intenta de nuevo.")
        print("Presiona ENTER para volver al menú.")
        input()
    
    
    
   
        
        
        

