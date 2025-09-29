import random # para poder usar el modulo random
# PENDIENTES
# corregir cuando pone cualquier otra cosa que no sea a b c o d en las opciones (TRIVIA)
# hacer que en medio de un juego pueda salir sin necesidad de terminarlo (solo falta en Trivia)
mostrar_menu = True # esta variable controla si se muestra el menu o no
while mostrar_menu == True:
    print("-"*18)
    print("  MENÚ DE JUEGOS  ")
    print("-"*18)
    print("")
    print("1. Piedra Papel o Tijera vs Computadora ✊✋✌️")
    print("2. Adivina el Número 🔢")
    print("3. Trivia Argentina 🧠🏆 ")
    print("0. Salir del programa 👋")
    print("")
    try: # este try funciona en caso de que se ingrese algo que NO SEA un número entero (ya sea un float o otro caracter)
        opcion_elegida = int(input("Elija un juego (ingresa el número) o '0' para salir: "))
        print("")
    except ValueError:
            print("")
            print("⚠️ OPCIÓN NO VALIDA, por favor ingrese un numero, ya sea 1,2,3,0⚠️")  
            print("")
            continue # hace que se reinicie el while mostrar_menu

    match opcion_elegida:

        case 1: # JUEGO 1 Piedra Papel o Tijera vs Computadora
            jugar_de_nuevo_1 = True
            while jugar_de_nuevo_1 == True: # mientras este variable sea true el juego se ejecuta de vuelta
                print("-"*67)
                print("Iniciando: 'Piedra Papel o Tijera vs Computadora' ¡Buena suerte! 🍀")
                print("-"*67)
                print("")
                turnos = 3 # contador de turnos en 3
                gano_usuario = 0 # rondas q gano usuario en 0
                gano_computadora = 0 # rondas que la compu gano
                salir_juego_1 = False
                while turnos > 0: # el juego no se termina hasta q se acaben los 3 turnos
                    try:
                        usuario = int(input("Elija una jugada 1. Piedra 2. Papel 3. Tijera (o '0' para salir): "))
                        if usuario == 0: # si ingresa 0 se sale del juego y vuelve al menu
                            salir_juego_1 = True
                            jugar_de_nuevo_1 = False
                            print("SALIENDO DEL JUEGO...")
                            print("")
                            break
                    except ValueError: # en caso de que se ingrese algo que no sea un nro entero
                        print("⚠️  ERROR: ingrese el número correspondiente a su jugada: 1, 2 o 3 ⚠️")
                        continue # se reinicia el while sin restar turnos
                    if usuario == 1:
                        jugada1 = "piedra"  # convertir las jugadas en palabras
                    elif usuario == 2:
                        jugada1 = "papel"
                    elif usuario == 3:
                        jugada1 = "tijera" 
                    computadora = random.randint(1,3) # generar jugada aleatoria de la computadora
                    if computadora == 1:
                        jugada2 = "piedra"  # convertir la jugada aleatoria en palabras
                    elif computadora == 2:
                        jugada2 = "papel"
                    elif computadora == 3:
                        jugada2 = "tijera"
                    if (usuario == 1 or usuario == 2 or usuario == 3):  # validar que el numero ingresado por el usuario sea 1,2 o 3
                        turnos -= 1  # restar un turno si la jugada del usuario es valida
                        if jugada1 == jugada2:  # en caso de empate 
                            print(f"EMPATE, ambos eligieron {jugada1}")
                        elif (jugada1 == "piedra" and jugada2 == "tijera") or \
                            (jugada1 == "papel" and jugada2 == "piedra") or \
                            (jugada1 == "tijera" and jugada2 == "papel"): # en caso de que gane el usuario
                            print(f"GANA {"USUARIO"} con {jugada1} contra {"computadora"} con {jugada2}")
                            gano_usuario += 1  # sumar una ronda ganada al usuario 
                        else: # en caso de que la compu gane
                            print(f"GANA {"COMPUTADORA"} con {jugada2} contra {"usuario"} con {jugada1}")
                            gano_computadora += 1  # sumar una ronda ganada a la compu
                    else:  # en caso de que la validación de la jugada que ingreso el usuario no sea valida (puso otro nro que no es 1,2,3,0)
                        print("⚠️  ERROR: ingrese el número correspondiente a su jugada: 1, 2 o 3 ⚠️") 
                    print("")
                if salir_juego_1 == False: 
                    if gano_usuario > gano_computadora:  
                        print(f"Ganador final: Usuario {gano_usuario} a {gano_computadora}")
                        print("¡Felicitaciones! 🎉")  # si el usuario le gana a la compu felicitarlo
                    elif gano_computadora > gano_usuario:
                        print(f"Ganador final: Computadora {gano_computadora} a {gano_usuario}")
                        print("¡La proxima sera! 💪")  # si el usuario pierde desearle suerte para la proxima
                    else:
                        print(f"Empate {gano_usuario} a {gano_computadora} 🤝")  # en caso de empate
                    print("") 
                    if usuario != 0: # si se termino la partida y el usuario no se salio preguntarle si desea volver a jugar
                        while jugar_de_nuevo_1 == True:
                            seguir_jugando_1 = input("Desea volver a jugar? y/n: ").lower()
                            print("")
                            if seguir_jugando_1 == "n": # si no quiere volver a jugar el ciclo while para jugar de nuevo no se inicia
                                print("FINALIZANDO EL JUEGO...")
                                print("")
                                jugar_de_nuevo_1 = False
                            elif seguir_jugando_1 == "y":
                                break  # si ingresa que si este ciclo while se termina y se vuelve a iniciar este juego
                            else:
                                print("⚠️ OPCIÓN NO VALIDA, por favor ingrese 'y' o 'n'⚠️")  # por si ingresa una opción no valida vuelve a preguntar                              
        
        case 2: # JUEGO 2 Adivina el número
            jugar_de_nuevo_2 = True
            while jugar_de_nuevo_2 == True:  # ciclo while que se ejecuta mientras el usuario vuelva a jugar este juego
                print("-"*48)
                print("Iniciando: 'Adivina el número' ¡Buena suerte! 🍀")
                print("-"*48)
                print("")
                pc_nro = random.randint(1, 15)  # numero aleatorio a adivinar 
                intentos = 3  # intentos máximos
                ganaste = False  # sino gana siempre va a estar en false 
                salir_juego_2 = False
                while intentos > 0 and ganaste == False:
                    try:
                        if intentos == 1: # simplemente quito las s si solo queda un intento
                            numero = int(input(f"Te queda {intentos} intento, Ingresa tu número del 1 al 15 (o '0' para salir): "))
                        else:
                            numero = int(input(f"Te quedan {intentos} intentos, Ingresa tu número del 1 al 15 (o '0' para salir): "))
                    except ValueError:
                        print("⚠️ ERROR: La entrada debe ser un número entre 1 y 15⚠️")  # en caso de que ingrese otra cosa que no sea un nro entero
                        continue # reinicia el while sin restar intentos
                    if numero == 0:
                        salir_juego_2 = True
                        jugar_de_nuevo_2 = False
                        print("SALIENDO DEL JUEGO...")
                        print("")
                        break               
                    if pc_nro == numero:
                        if intentos == 3:
                            print("¡A LA PRIMERA ADIVINASTE!, LOCURAAAA 🤯")  # en caso de que adivine a la primera
                        else:
                            print("¡ADIVINASTE GENI@, FELICITACIONES! 🎊")  # en caso de que adivine en otro intento
                        ganaste = True 
                    else:  # restar un intentos si el nro de usuario no es igual al nro del programa
                        intentos -= 1 
                        if intentos >=1:
                            if numero < pc_nro:
                                print("INCORRECTO, intenta con un numero mas grande")  # pistas para ayudar al usuario 
                            else:
                                print("INCORRECTO, intenta con un numero mas chico")
                if salir_juego_2 == False:
                    if ganaste == False:  # en caso de que no hay ganado muestra cual era el nro
                        print(f"Perdiste. El número era {pc_nro} 😅")
                    print("")
                    while jugar_de_nuevo_2 == True:                        
                        seguir_jugando_2 = input("Desea volver a jugar? y/n: ").lower()  # al terminar la partida haya ganado o no le pregunta si desea volver a jugar
                        print("")
                        if seguir_jugando_2 == "n":
                            print("FINALIZANDO EL JUEGO...")
                            print("")
                            jugar_de_nuevo_2 = False
                        elif seguir_jugando_2 == "y":
                            break  # si ingresa que si este ciclo while se termina y se vuelve a iniciar este juego
                        else:
                            print("⚠️ OPCIÓN NO VALIDA, por favor ingrese 'y' o 'n'⚠️")  # por si ingresa una opción no valida vuelve a preguntar
        
        case 3: # JUEGO 3 Trivia de Argentina
            jugar_de_nuevo_3 = True  # al terminar de jugar puede elegir si salir al menu o jugar de vuelta este juego
            while jugar_de_nuevo_3 == True:
                print("-"*47)
                print("Iniciando: 'Trivia Argentina' ¡Buena suerte! 🍀")
                print("-"*47)
                pregunta1_usada = False  # estas variables controlan si la pregunta ya apareció, si apareció cambia su estado a True
                pregunta2_usada = False
                pregunta3_usada = False
                pregunta4_usada = False
                pregunta5_usada = False
                pregunta6_usada = False
                pregunta7_usada = False
                pregunta8_usada = False
                pregunta9_usada = False 
                pregunta10_usada = False
                pregunta11_usada = False
                pregunta12_usada = False
                pregunta13_usada = False
                pregunta14_usada = False
                pregunta15_usada = False
                acertadas = 0
                for i in range(15):  # en un ciclo de 15 iteraciones se va a generar un nro al azar que corresponde a una pregunta
                    orden = random.randint(1, 15)
                    while (orden == 1 and pregunta1_usada == True) or \
                        (orden == 2 and pregunta2_usada == True) or \
                        (orden == 3 and pregunta3_usada == True) or \
                        (orden == 4 and pregunta4_usada == True) or \
                        (orden == 5 and pregunta5_usada == True) or \
                        (orden == 6 and pregunta6_usada == True) or \
                        (orden == 7 and pregunta7_usada == True) or \
                        (orden == 8 and pregunta8_usada == True) or \
                        (orden == 9 and pregunta9_usada == True) or \
                        (orden == 10 and pregunta10_usada == True) or \
                        (orden == 11 and pregunta11_usada == True) or \
                        (orden == 12 and pregunta12_usada == True) or \
                        (orden == 13 and pregunta13_usada == True) or \
                        (orden == 14 and pregunta14_usada == True) or \
                        (orden == 15 and pregunta15_usada == True):  # si el nro (la pregunta) ya apareció antes, se genera un nro nuevo
                        orden = random.randint(1, 15)
                    print("")
                    match orden:  # va a imprimir la pregunta y sus respuesta según el caso (nro) que salga en la variable orden
                        case 1:
                            print("¿Cuál es el gentilicio de los habitantes de la ciudad de Buenos Aires?")
                            print("a) Bonaerense b) Porteño c) Bonaireño d) Airense")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()  # por si ingresa mayúscula lo convierte a minúscula
                            respuesta_correcta = "b"
                            pregunta1_usada = True  # al aparecer esta pregunta (o cualquier otra obvio) esta variable pasa de estado False a True
                        case 2:
                            print("¿Cuántas provincias tiene Argentina?")
                            print("a) 22 b) 23 c) 24 d) 25")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()   
                            respuesta_correcta ="b"
                            pregunta2_usada = True
                        case 3:
                            print("¿Cuál es la provincia más pequeña de Argentina?")
                            print("a) Tucumán b) Jujuy c) Misiones  d) Entre Rios")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta ="a"
                            pregunta3_usada = True
                        case 4:
                            print("¿Cuál de estos famosos autores NO es argentino?")
                            print("a) Julio Cortázar b) Pablo Neruda c) Jorge Luis Borges d) Alejandra Pizarnik")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "b"
                            pregunta4_usada = True
                        case 5:
                            print("¿En qué fecha se independizó Argentina?")
                            print("a) 9 de junio de 1816 b) 9 de julio de 1916 c) 9 de junio de 1916 d) 9 de julio de 1816")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta ="d"
                            pregunta5_usada = True
                        case 6:
                            print("¿Cuál de las siguientes montañas, es la más alta del continente americano?")
                            print("a) El volcán Llullaillaco, en Salta. b) El nevado Tres Cruces, en Catamarca. c) El cerro Aconcagua, en Mendoza. d) El cerro Ramada, en San Juan.")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "c"
                            pregunta6_usada = True
                        case 7:
                            print("¿Con cuántos países limita Argentina?")
                            print("a) 2 b) 3 c) 4 d) 5")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "d"
                            pregunta7_usada = True
                        case 8:
                            print("¿En qué años tuvo lugar la dictadura militar?")
                            print("a) 1970 a 1987 b) 1978 a 1980 c) 1972 a 1984 d) 1976 a 1983")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "d"
                            pregunta8_usada = True
                        case 9:
                            print("¿Dónde se encuentra la región patagónica?")
                            print("a) En el norte b) En el oeste c) En el sur d) En el centro")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "c"
                            pregunta9_usada = True
                        case 10:
                            print("¿Cómo se le conoce a la selección de fútbol argentina?")
                            print("a) La del che b) La albiceleste c) Los tangos d) La fiera celeste")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "b"
                            pregunta10_usada = True
                        case 11:
                            print("¿Cuál es el nombre de la famosa niña de la historieta de Quino?")
                            print("a) Matilda  b) Mafalda c) Susanita d) Manuelita")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "b"
                            pregunta11_usada = True
                        case 12:
                            print("¿Por que es famoso el rio de la plata?")
                            print("a) Mas ancho del mundo b) Mas claro del mundo c) Mas largo del mundo d) Mas hermoso del mundo")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "a"
                            pregunta12_usada = True
                        case 13:
                            print("¿Cuantos premios Nobel han sido ganados por argentinos?")
                            print("a) 2 b) 3 c) 4 d) 5")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "d"
                            pregunta13_usada = True
                        case 14:
                            print("¿Cuantos golpes de estado hubo en Argentina?")
                            print("a) 3 b) 5 c) 6 d) 8")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "c"
                            pregunta14_usada = True
                        case 15:
                            print("¿Cual es la principal exportación de Argentina?")
                            print("a) Soja b) Petroleo c) Mani d) Oro")
                            respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                            respuesta_correcta = "a"
                            pregunta15_usada = True
                    if respuesta_usuario == respuesta_correcta:
                        print("✅¡CORRECTOOO!✅")
                        acertadas += 1  # si la respuesta es correcta imprimimos este msj y con un contador sumamos 1 a las preguntas acertadas
                    else:
                        print(f"❌INCORRECTO❌ La respuesta era la {respuesta_correcta})")  # si la respuesta es incorrecta, se muestra la respuesta correcta
                print("")
                if acertadas == 15:  # según la cantidad de preguntas acertadas va a mostrar cierto mensaje
                    print(f"15/15: 🏆👑 ¡PERFECTO!")
                elif acertadas >= 10 and acertadas <= 14:
                    print(f"{acertadas}/15: 🎉😊 ¡Muy bien!")
                elif acertadas >= 5 and acertadas <= 9:
                    print(f"{acertadas}/15: 📖💪 ¡Sigue intentando!")
                else:
                    print(f"{acertadas}/15: 🤔📚 ¡No te rindas!")
                print("")
                while jugar_de_nuevo_3 == True:
                    seguir_jugando_3 = input("Desea volver a jugar? y/n: ").lower()  # para salir al menu o volver a jugar
                    if seguir_jugando_3 == "n":
                        print("FINALIZANDO EL JUEGO...")
                        print("")
                        jugar_de_nuevo_3 = False
                    elif seguir_jugando_3 == "y":
                        break  # si ingresa que si este ciclo while se termina y se vuelve a iniciar este juego
                    else:
                        print("⚠️ OPCIÓN NO VALIDA, por favor ingrese 'y' o 'n'⚠️")  # por si ingresa una opción no valida vuelve a preguntar
        
        case 0:
            print("FINALIZANDO EL PROGRAMA...")
            mostrar_menu = False  # si en el menu se ingresa el nro cero se sale del programa definitivamente
        
        case _: # este case funciona en caso de que se ingrese algún otro numero que no sea 1,2,3,0
            print("⚠️ OPCIÓN NO VALIDA, por favor ingrese un numero, ya sea 1,2,3,0⚠️") 
            print("")