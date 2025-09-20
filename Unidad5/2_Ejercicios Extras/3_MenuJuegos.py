import random
print("-"*18)
print("  MENÚ DE JUEGOS  ")
print("-"*18)
print("")
print("1. Trivia Argentina")
print("2. Adivina el Número")
print("3. Piedra Papel o Tijera vs Computadora")
print("0. Salir")
print("")
opcion_elegida = input("Elige un juego (ingresa el número) o '0' para salir: ")
print("")
if opcion_elegida == "3":
    no_seguir_3 = False
    while no_seguir_3 == False:
        print("-"*64)
        print("Iniciando: 'Piedra Papel o Tijera vs Computadora' ¡Buena suerte!")
        print("-"*64)
        print("")
        usuario = int(input("Eliga una jugada (ingrese el número) 1. Piedra 2. Papel 3. Tijera : "))
        if usuario == 1:
            jugada1 = "piedra"
        elif usuario == 2:
            jugada1 = "papel"
        elif usuario == 3:
            jugada1 = "tijera"
        computadora = random.randint(1,3)
        if computadora == 1:
            jugada2 = "piedra"
        elif computadora == 2:
            jugada2 = "papel"
        elif computadora == 3:
            jugada2 = "tijera"
        if (usuario == 1 or usuario == 2 or usuario == 3):
            if jugada1 == jugada2:
                print(f"EMPATE, ambos eligieron {jugada1}")
            elif (jugada1 == "piedra" and jugada2 == "tijera") or \
                (jugada1 == "papel" and jugada2 == "piedra") or \
                (jugada1 == "tijera" and jugada2 == "papel"):
                print(f"GANA {"USUARIO"} con {jugada1} contra {"computadora"} con {jugada2}")
            else:
                print(f"GANA {"COMPUTADORA"} con {jugada2} contra {"usuario"} con {jugada1}")
        else:
            print("La jugada ingresada NO es valida")
        print("")
        seguir_jugando_3 = input("Desea volver a jugar? y/n: ")
        match seguir_jugando_3:
            case "y":
                no_seguir_3 = False
            case "n":
                no_seguir_3 = True
                print(f"FINALIZANDO EL PROGRAMA...")
elif opcion_elegida == "2":
    no_seguir_2 = False
    while no_seguir_2 == False:
        print("-"*45)
        print("Iniciando: 'Adivina el número' ¡Buena suerte!")
        print("-"*45)
        print("")
        pc_nro = random.randint(1, 15)
        intentos = 3
        ganaste = False
        while intentos > 0 and not ganaste:
            if intentos == 1:
                numero = int(input(f"Te queda {intentos} intento, Ingresa tu número del 1 al 15: "))
            else:
                numero = int(input(f"Te quedan {intentos} intentos, Ingresa tu número del 1 al 15: "))
            if pc_nro == numero:
                if intentos == 3:
                    print("¡A LA PRIMERA ADIVINASTE!, LOCURAAAA")
                else:
                    print("¡ADIVINASTE GENI@, FELICITACIONES!")
                ganaste = True
            else:
                intentos -= 1
                if intentos >=1:
                    if numero < pc_nro:
                        print("INCORRECTO, intenta con un numero mas grande")
                    else:
                        print("INCORRECTO, intenta con un numero mas chico")
        if not ganaste:
            print(f"Perdiste. El número era {pc_nro}")
        print("")
        seguir_jugando_2 = input("Desea volver a jugar? y/n: ")
        match seguir_jugando_2:
            case "y":
                no_seguir_2 = False
            case "n":
                no_seguir_2 = True
                print(f"FINALIZANDO EL PROGRAMA...")
elif opcion_elegida == "1":
    no_seguir_1 = False
    while no_seguir_1 == False:
        print("-"*44)
        print("Iniciando: 'Trivia Argentina' ¡Buena suerte!")
        print("-"*44)
        print("")
        pregunta1_usada = False
        pregunta2_usada = False
        pregunta3_usada = False
        pregunta4_usada = False
        pregunta5_usada = False
        pregunta6_usada = False
        pregunta7_usada = False
        for i in range(7):
            orden = random.randint(1, 7)
            while (orden == 1 and pregunta1_usada == True) or \
                (orden == 2 and pregunta2_usada == True) or \
                (orden == 3 and pregunta3_usada == True) or \
                (orden == 4 and pregunta4_usada == True) or \
                (orden == 5 and pregunta5_usada == True) or \
                (orden == 6 and pregunta6_usada == True) or \
                (orden == 7 and pregunta7_usada == True):
                orden = random.randint(1, 7)
            print("")
            match orden:
                    case 1:
                        print("¿Cuál es el gentilicio de los habitantes de la ciudad de Buenos Aires?")
                        print("1) Bonaerense 2) Porteño 3) Bonaireño 4) Airense")
                        respuesta_1 = int(input("Ingrese el numero de la opcion correcta: "))
                        if respuesta_1 == 2:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta1_usada = True
                    case 2:
                        print("¿Cuántas provincias tiene Argentina?")
                        print("1) 24  2) 22 3) 25 4) 23")
                        respuesta_2 = int(input("Ingrese el numero de la opcion correcta: "))   
                        if respuesta_2 == 4:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta2_usada = True
                    case 3:
                        print("¿Cuál es la provincia más pequeña de Argentina?")
                        print("1) Mendoza 2) Salta 3) Tucumán 4) Rosario")
                        respuesta_3 = int(input("Ingrese el numero de la opcion correcta: "))
                        if respuesta_3 == 3:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta3_usada = True
                    case 4:
                        print("¿Cuál de estos famosos autores NO es argentino?")
                        print("1) Julio Cortázar 2) Pablo Neruda 3) Jorge Luis Borges 4) Alejandra Pizarnik")
                        respuesta_4 = int(input("Ingrese el numero de la opcion correcta: "))
                        if respuesta_4 == 2:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta4_usada = True
                    case 5:
                        print("¿En qué fecha se independizó Argentina?")
                        print("1) 9 de junio de 1816 2) 9 de julio de 1916 3) 9 de junio de 1916 4) 9 de julio de 1816")
                        respuesta_5 = int(input("Ingrese el numero de la opcion correcta: "))
                        if respuesta_5 == 4:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta5_usada = True
                    case 6:
                        print("En Argentina se halla la montaña más alta del continente americano ¿cuál es?")
                        print("1) El volcán Llullaillaco, en Salta. 2) El nevado Tres Cruces, en Catamarca. 3) El cerro Aconcagua, en Mendoza. 4) El cerro Ramada, en San Juan.")
                        respuesta_6 = int(input("Ingrese el numero de la opcion correcta: "))
                        if respuesta_6 == 3:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta6_usada = True
                    case 7:
                        print("¿Con cuántos países comparte Argentina fronteras terrestres?")
                        print("1) 3  2) 4 3) 5 4) 2")
                        respuesta_7 = int(input("Ingrese el numero de la opcion correcta: "))
                        if respuesta_7 == 3:
                            print("CORRECTOOO")
                        else:
                            print("INCORRECTO")
                        pregunta7_usada = True
        print("")
        seguir_jugando_1 = input("Desea volver a jugar? y/n: ")
        match seguir_jugando_1:
            case "y":
                no_seguir_1 = False
            case "n":
                no_seguir_1 = True
                print(f"FINALIZANDO EL PROGRAMA...")    
elif opcion_elegida == "0":
    print(f"FINALIZANDO EL PROGRAMA...")
else:
    print(f"Opcion no valida, por favor revise la entrada")