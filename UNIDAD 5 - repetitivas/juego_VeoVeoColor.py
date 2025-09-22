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