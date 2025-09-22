import random
# PENDIENTE
# corregir cuando pone 'enter' en las opciones (TRIVIA)
# hacer que en medio de un juego pueda salir sin necesidad de terminarlo
# mostrar el menú al salir de un juego
print("-"*18)
print("  MENÚ DE JUEGOS  ")
print("-"*18)
print("")
print("1. Piedra Papel o Tijera vs Computadora")
print("2. Adivina el Número")
print("3. Trivia Argentina")
print("0. Salir del programa")
print("")
opcion_elegida = input("Elige un juego (ingresa el número) o '0' para salir: ")
print("")
match opcion_elegida:
    case "1":
        jugar_de_nuevo_1 = True
        while jugar_de_nuevo_1 == True:
            print("-"*64)
            print("Iniciando: 'Piedra Papel o Tijera vs Computadora' ¡Buena suerte!")
            print("-"*64)
            print("")
            turnos = 3
            gano_usuario = 0
            gano_computadora = 0
            while turnos > 0:
                try:
                    usuario = int(input("Eliga una jugada (ingrese el número) 1. Piedra 2. Papel 3. Tijera : "))
                except ValueError:
                    print("ERROR: ingrese el número correspondiente a su jugada: 1, 2 o 3")
                    continue
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
                    turnos -= 1
                    if jugada1 == jugada2:
                        print(f"EMPATE, ambos eligieron {jugada1}")
                    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
                        (jugada1 == "papel" and jugada2 == "piedra") or \
                        (jugada1 == "tijera" and jugada2 == "papel"):
                        print(f"GANA {"USUARIO"} con {jugada1} contra {"computadora"} con {jugada2}")
                        gano_usuario += 1
                    else:
                        print(f"GANA {"COMPUTADORA"} con {jugada2} contra {"usuario"} con {jugada1}")
                        gano_computadora += 1
                else:
                    print("ERROR: ingrese el número correspondiente a su jugada: 1, 2 o 3")
                print("")
            if gano_usuario > gano_computadora:
                print(f"Ganador final: Usuario {gano_usuario} a {gano_computadora}")
                print("¡Felicitaciones!")
            elif gano_computadora > gano_usuario:
                print(f"Ganador final: Computadora {gano_computadora} a {gano_usuario}")
                print("¡La proxima sera!")
            else:
                print(f"Empate {gano_usuario} a {gano_computadora}")
            print("")
            seguir_jugando_1 = input("Desea volver a jugar? y/n: ")
            print("")
            match seguir_jugando_1:
                case "n":
                    print("FINALIZANDO EL JUEGO...")
                    jugar_de_nuevo_1 = False
    case "2":
        jugar_de_nuevo_2 = True
        while jugar_de_nuevo_2 == True:
            print("-"*45)
            print("Iniciando: 'Adivina el número' ¡Buena suerte!")
            print("-"*45)
            print("")
            pc_nro = random.randint(1, 15)
            intentos = 3
            ganaste = False
            while intentos > 0 and not ganaste:
                try:
                    if intentos == 1:
                        numero = int(input(f"Te queda {intentos} intento, Ingresa tu número del 1 al 15: "))
                    else:
                        numero = int(input(f"Te quedan {intentos} intentos, Ingresa tu número del 1 al 15: "))
                except ValueError:
                    print("ERROR: La entrada debe ser un número entre 1 y 15")
                    continue
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
            print("")
            match seguir_jugando_2:
                case "n":
                    jugar_de_nuevo_2 = False
                    print("FINALIZANDO EL JUEGO...")
    case "3":
        jugar_de_nuevo_3 = True
        while jugar_de_nuevo_3 == True:
            print("-"*44)
            print("Iniciando: 'Trivia Argentina' ¡Buena suerte!")
            print("-"*44)
            pregunta1_usada = False
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
            for i in range(15):
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
                    (orden == 15 and pregunta15_usada == True):
                    orden = random.randint(1, 15)
                print("")
                match orden:
                    case 1:
                        print("¿Cuál es el gentilicio de los habitantes de la ciudad de Buenos Aires?")
                        print("a) Bonaerense b) Porteño c) Bonaireño d) Airense")
                        respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                        respuesta_correcta = "b"
                        pregunta1_usada = True
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
                        respuesta_usuario = input("Ingrese la letra de la opcion correcta: ").lower()
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
                        print("¿Cual es la principal exportacion de Argentina?")
                        print("a) Soja b) Petroleo c) Mani d) Oro")
                        respuesta_usuario = input("Ingrese la letra de la opción correcta: ").lower()
                        respuesta_correcta = "a"
                        pregunta15_usada = True
                if respuesta_usuario == respuesta_correcta:
                    print("¡CORRECTOOO! ✅")
                    acertadas += 1
                else:
                    print(f"INCORRECTO ❌ La respuesta era la {respuesta_correcta})")
            print("")    
            print(f"El total de preguntas acertadas es de {acertadas}/15")
            print("")
            seguir_jugando_3 = input("Desea volver a jugar? y/n: ").lower()
            print("")
            match seguir_jugando_3:
                case "n":
                    jugar_de_nuevo_3 = False
                    print("FINALIZANDO EL JUEGO...")
    case "0":
        print(f"FINALIZANDO EL PROGRAMA...")
    case _:
        print(f"Opcion no valida, por favor revise la entrada")