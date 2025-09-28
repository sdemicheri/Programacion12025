print("Menu de juegos")
print(" 1- Cara o Cruz")
print(" 2- Adivina el numero")
print(" 3- Veo Veo colores")

print("0- Salir del programa")

opcion = int(input("Elija un juego o 0 para salir: "))

match opcion :
    case 1:
        import random

        print("Bienvenido al juego de Cara o Cruz!")

        while True:  # bucle principal
            respuesta_inicio = input("¿Estás listo para jugar? (si/no): ")

            if respuesta_inicio == "si":
                # El jugador elige
                eleccion = input("Elegí: cara o cruz: ")

                # La compu lanza la moneda
                moneda = random.choice(["cara", "cruz"])

                print(f"La moneda cayó en: {moneda}")

                # Verificar si ganó
                if eleccion == moneda:
                    print("Bien, ganaste!")
                else:
                    print("No, perdiste")

            elif respuesta_inicio == "no":
                print("Nos vemos la proxima, gracias!")
                break  # salir del bucle principal

            else:
                print("Respuesta inválida. Escribí 'si' o 'no'.\n")




    case 2:
    import random
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("Hola vamos a jugar! yo elijo un numero y vos adivinas cual es!")
    print("Estoy pensando en un número del 1 al 10. ¿Crees saber cual?")

    while True:
        try:
            # Pedir número al jugador
            adivinanza = int(input("Ingresa tu número: "))
            intentos += 1
            
            if adivinanza < 1 or adivinanza > 10:
                print("Por favor, ingresa un número entre 1 y 10.")
                continue

            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta otra vez.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta otra vez.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos")
                break
        except ValueError:
            print("Entrada inválida. Ingresa un número del 1 al 10.")


    case 3:

    import random
    colores_primarios = ["Rojo", "Azul", "Amarillo"]
    colores_secundarios = ["Verde", "Naranja", "Violeta"]
    colores = colores_primarios + colores_secundarios

    print("¡Bienvenidos al VEO VEO de colores primarios y secundarios!")

    while True:  # bucle principal, se repite hasta que el jugador diga "no"
        pregunta_inicio = input("¿Querés jugar al VEO VEO de colores? (si/no): ")

        if pregunta_inicio == "si":
            # Configuración de intentos
            max_intentos = 3
            intentos_restantes = max_intentos
            indice_pista = 0

            # La compu elige un color al azar
            color_secreto = random.choice(colores)

            # Lista de pistas
            pistas = [
                f"Pista 1: El color empieza con la letra '{color_secreto[0]}'",
                f"Pista 2: El color tiene {len(color_secreto)} letras",
                f"Pista 3: Es un color {'primario' if color_secreto in colores_primarios else 'secundario'}"
            ]
            print("Tienen 3 intentos para adivinar el color secreto.\n")

            # Juego
            while intentos_restantes > 0:
                print(pistas[indice_pista])
                respuesta = input("¿Cuál es tu respuesta?: ")

                if respuesta == color_secreto:  # comparación exacta
                    print("Siiii!!!")
                    break
                else:
                    intentos_restantes -= 1
                    indice_pista += 1
                    if intentos_restantes > 0:
                        print("No es correcto, intenta otra vez.\n")

            if intentos_restantes == 0 and respuesta != color_secreto:
                print(f"Perdiste. El color era {color_secreto}.")

        elif pregunta_inicio == "no":
            print("Está bien ¡gracias por jugar!")
            break  # salir del bucle principal

        else:
            print("Respuesta inválida. Escribí 'si' o 'no'.")
