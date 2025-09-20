import random
print("-"*18)
print("  MENÚ DE JUEGOS  ")
print("-"*18)
print("")
print("1. Trivia Argentina")
print("2. Adivina el Número")
print("3. Piedra Papel o Tijera vs Computadora")
print("")
opcion_elegida = input("Elige un juego (ingresa el número) o '0' para salir: ")
print("")
if opcion_elegida == "1":
    print("-"*44)
    print("Iniciando: 'Trivia Argentina' ¡Buena suerte!")
    print("-"*44)
    print("")
elif opcion_elegida == "2":
    print("-"*45)
    print("Iniciando: 'Adivina el número' ¡Buena suerte!")
    print("-"*45)
    print("")
elif opcion_elegida == "3":
    print("-"*64)
    print("Iniciando: 'Piedra Papel o Tijera vs Computadora' ¡Buena suerte!")
    print("-"*64)
    print("")
elif opcion_elegida == "0":
    print(f"FINALIZANDO EL PROGRAMA...")
else:
    print(f"Opcion no valida, por favor revise la entrada")
if opcion_elegida == "3":
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
elif opcion_elegida == "2":
    pc_nro = random.randint(1, 10)
    intentos = 3
    ganaste = False
    while intentos > 0 and not ganaste:
        if intentos == 1:
            numero = int(input(f"Te queda {intentos} intento, Ingresa tu número del 1 al 10: "))
        else:
            numero = int(input(f"Te quedan {intentos} intentos, Ingresa tu número del 1 al 10: "))
        if pc_nro == numero:
            if intentos == 3:
                print("¡A LA PRIMERA ADIVINASTE!, LOCURAAAA")
            else:
                print("¡ADIVINASTE GENI@, FELICITACIONES!")
            ganaste = True
        else:
            intentos -= 1
            if numero < pc_nro:
                print("INCORRECTO, intenta con un numero mas grande")
            else:
                print("INCORRECTO, intenta con un numero mas chico")
    if not ganaste:
        print(f"Perdiste. El número era el {pc_nro}")
elif opcion_elegida == "1":
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
        if orden == 1:
            pregunta1_usada = True
        elif orden == 2:
            pregunta2_usada = True
        elif orden == 3:
            pregunta3_usada = True
        elif orden == 4:
            pregunta4_usada = True
        elif orden == 5:
            pregunta5_usada = True
        elif orden == 6:
            pregunta6_usada = True
        elif orden == 7:
            pregunta7_usada = True
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
                case 2:
                    print("¿Cuántas provincias tiene Argentina?")
                    print("1) 24  2) 22 3) 25 4) 23")
                    respuesta_2 = int(input("Ingrese el numero de la opcion correcta: "))   
                    if respuesta_2 == 4:
                        print("CORRECTOOO")
                    else:
                        print("INCORRECTO")
                case 3:
                    print("¿Cuál es la provincia más pequeña de Argentina?")
                    print("1) Mendoza 2) Salta 3) Tucumán 4) Rosario")
                    respuesta_3 = int(input("Ingrese el numero de la opcion correcta: "))
                    if respuesta_3 == 3:
                        print("CORRECTOOO")
                    else:
                        print("INCORRECTO")
                case 4:
                    print("¿Cuál de estos famosos autores NO es argentino?")
                    print("1) Julio Cortázar 2) Pablo Neruda 3) Jorge Luis Borges 4) Alejandra Pizarnik")
                    respuesta_4 = int(input("Ingrese el numero de la opcion correcta: "))
                    if respuesta_4 == 2:
                        print("CORRECTOOO")
                    else:
                        print("INCORRECTO")
                case 5:
                    print("¿En qué fecha se independizó Argentina?")
                    print("1) 9 de junio de 1816 2) 9 de julio de 1916 3) 9 de junio de 1916 4) 9 de julio de 1816")
                    respuesta_5 = int(input("Ingrese el numero de la opcion correcta: "))
                    if respuesta_5 == 4:
                        print("CORRECTOOO")
                    else:
                        print("INCORRECTO")
                case 6:
                    print("En Argentina se halla la montaña más alta del continente americano ¿cuál es?")
                    print("1) El volcán Llullaillaco, en Salta. 2) El nevado Tres Cruces, en Catamarca. 3) El cerro Aconcagua, en Mendoza. 4) El cerro Ramada, en San Juan.")
                    respuesta_6 = int(input("Ingrese el numero de la opcion correcta: "))
                    if respuesta_6 == 3:
                        print("CORRECTOOO")
                    else:
                        print("INCORRECTO")
                case 7:
                    print("¿Con cuántos países comparte Argentina fronteras terrestres?")
                    print("1) 3  2) 4 3) 5 4) 2")
                    respuesta_7 = int(input("Ingrese el numero de la opcion correcta: "))
                    if respuesta_7 == 3:
                        print("CORRECTOOO")
                    else:
                        print("INCORRECTO")