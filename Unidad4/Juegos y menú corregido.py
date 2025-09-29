salir = False
while salir == False:
        try:
            print("-"*20)
            print("Bienvenido al menú principal")
            print("1) Piedra, papel o tijeras")
            print("2) Preguntas y respuestas")
            print("3) Adivina el número")
            print("4) Salir")
            print("-"*20)
            opcion = int(input("Elige una opcion del 1 al 4: "))
        except ValueError:
            print("Ingresó un dato incorrecto. Intente de nuevo")
            continue
        if opcion == 1:
                print("-"*15)
                print("Bienvenidos a Piedra, Papel o Tijera ")
                print("Opciones: ")
                print("1 Piedra")
                print("2 Papel")
                print("3 Tijera")
                print("-"*15)
                ganador = False
                while ganador == False:
                    try:
                        jugador1=int(input("Jugador 1, elige una opción del 1 al 3 "))
                        jugador2=int(input("Jugador 2, elige una opción del 1 al 3 "))
                        if jugador1 < 1 or jugador1 > 3 or jugador2 < 1 or jugador2 > 3:
                            print("Ingresó un dato incorrecto")
                        elif jugador1 == jugador2:
                            print("Empate, jueguen de nuevo ")
                        elif jugador1 == 1 and jugador2 == 3 or jugador1 == 2 and jugador2 == 1 or jugador1 == 3 and jugador2 == 2:
                            print("El ganador es el jugador 1")
                            ganador = True
                        else:
                            print("El ganador es jugador 2")
                            ganador = True
                    except ValueError:
                        print("Ingresó un dato no válido. Vuelva a intentarlo")
        elif opcion == 2:
            try:
                print("-"*15)
                print("Pongamos a prueba tu conocimiento")
                print("-"*15)
                puntaje = 0
                print("Pregunta 1: ¿Cuál es la isla mas grande del planeta?")
                print("1) Islandia")
                print("2) Japón")
                print("3) Australia")
                print("4) Groenlandia")
                respuesta = int(input("Seleccione una opción "))
                if respuesta < 1 or respuesta > 4:
                    print("Ingreso una respuesta incorrecta ")
                elif respuesta == 4:
                    print("Correcto")
                    puntaje += 1
                else:
                    print("Respuesta incorrecta, la correcta era: Groenlandia")
                print("Pregunta 2: ¿Quién ganó el mundial 2002?")
                print("1) Brasil")
                print("2) Inglaterra")
                print("3) Francia")
                print("4) Alemania")
                respuesta = int(input("Seleccione una opción "))
                if respuesta == 1:
                    print("Correcto")
                    puntaje += 1
                else:
                    print("Respuesta incorrecta, la correcta era: Brasil")
                print("Pregunta 3: ¿Cuando llegó Cristóbal Colón a América?")
                print("1) 1492")
                print("2) 1453")
                print("3) 1500")
                print("4) 1473")
                respuesta = int(input("Seleccione una opción "))
                if respuesta == 1:
                    print("Correcto")
                    puntaje += 1
                else:
                    print("Respuesta incorrecta, la correcta era: 1492")
                print("Pregunta 3: ¿Cuál es el río mas largo del mundo?")
                print("1) Missisippi")
                print("2) Amazonas")
                print("3) Nilo")
                print("4) Calamuchita")
                respuesta = int(input("Seleccione una opción "))
                if respuesta == 2:
                    print("Correcto")
                    puntaje += 1
                else:
                    print("Respuesta incorrecta, la correcta era: Amazonas") 
                print("Pregunta 4: ¿Cuál es el planeta mas grande del sistema solar?")
                print("1) Neptuno")
                print("2) Saturno")
                print("3) Júpiter")
                print("4) Marte")
                respuesta = int(input("Seleccione una opción "))
                if respuesta == 3:
                    print("Correcto")
                    puntaje += 1
                else:
                    print("Respuesta incorrecta, la correcta era: Júpiter")
                print("Pregunta 5: ¿Qué elemento de la tabla periódica es este: Au?")
                print("1) Plata")
                print("2) Cobre")
                print("3) Aluminio")
                print("4) Oro")
                respuesta = int(input("Seleccione una opción "))
                if respuesta == 4:
                    print("Correcto")
                    puntaje += 1
                else:
                    print("Respuesta incorrecta, la correcta era: Oro")
                if puntaje == 6:
                    print("Respondiste correctamente a todas las preguntas. Excelente")
                elif puntaje >= 3 and puntaje <= 5:
                    print("Respondiste casi todas. Muy bien")
                elif puntaje <= 1 and puntaje <= 3:
                    print("Estuviste medio flojo, pero se puede mejorar. ¡Ánimo!")
                else:
                    print("Biennn, solo te faltó acertar todas las preguntas...Casi.")
            except ValueError:
                print("Ingresaste un dato no válido")
        elif opcion == 3:
            import random
            try:
                print("-"*15)
                print("Bienvenido a Adivina el número")
                print("La consola, tu archienemiga en este juego pensó un número del 1 al 20...¿te atreves a retarla?")
                print("-"*15)
                numero_secreto = random.randint(1,20)
                intentos = 0 
                adivinado = False
                while adivinado == False:
                    intento= int(input("Ingresa el número que pensaste: "))
                    intentos += 1
                    if intento < 0:
                        print("Tiene que ingresar un número del 1 al 20")
                    elif intento == numero_secreto:
                        print("Correcto, el número era",numero_secreto)
                        print("Lo conseguiste en",intentos,"intentos")
                        adivinado = True
                    elif intento < numero_secreto:
                        print("El número secreto es mayor")
                    else:
                        print("El número secreto es menor")
            except ValueError:
                print("Dato no válido")
        elif opcion == 4:
            print("Gracias por jugar")
            salir = True           