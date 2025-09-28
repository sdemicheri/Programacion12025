import random

# ---- MENÚ PRINCIPAL ----
print("---------------------------------------------")
print("      🎮 MENÚ DE JUEGOS 🎮")
print("---------------------------------------------")
print("1 - Cara o Cruz")
print("2 - Adivina el número")
print("3 - Veo Veo de Colores")
print("0 - Salir del programa")
print("---------------------------------------------")

opcion = int(input("Elige un juego (1-3) o 0 para salir: "))

# ---- JUEGO 1: Cara o Cruz ----
if opcion == 1:
    print("\n=== Juego 1: ☺️ Cara o Cruz 😵 ===")
    while True:
        respuesta_inicio = input("¿Estás listo para jugar? (si/no): ").lower()

        if respuesta_inicio == "si":
            eleccion = input("Elegí: cara o cruz: ").lower()
            moneda = random.choice(["cara", "cruz"])
            print(f"La moneda cayó en: {moneda}")

            if eleccion == moneda:
                print("¡Ganaste! 🎉")
            else:
                print("Perdiste 😢")
        elif respuesta_inicio == "no":
            print("Nos vemos la próxima, gracias por jugar!")
            break
        else:
            print("Respuesta inválida. Escribí 'si' o 'no'.")

# ---- JUEGO 2: Adivina el número ----
elif opcion == 2:
    print("\n=== Juego 2: Adivina el número ===")
    numero_secreto = random.randint(1, 10)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Adivina un número del 1 al 10: "))
            intentos += 1

            if adivinanza < 1 or adivinanza > 10:
                print("Número fuera de rango. Intenta entre 1 y 10.")
            elif adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"🎉 ¡Correcto! Lo adivinaste en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada incorrecta. Por favor ingresa un número.")

# ---- JUEGO 3: Veo Veo de colores ----
elif opcion == 3:
    print("\n=== Juego 3: Veo Veo de Colores 🎨 ===")
    colores_primarios = ["Rojo", "Azul", "Amarillo 🔴 🔵 🟡"]
    colores_secundarios = ["Verde", "Naranja", "Violeta 🟠🟢🟣  "]
    colores = colores_primarios + colores_secundarios

    jugar = input("¿Querés jugar al Veo Veo? (si/no): ").lower()
    if jugar == "si":
        color_secreto = random.choice(colores)
        pistas = [
            f"Pista 1: Empieza con '{color_secreto[0]}'",
            f"Pista 2: Tiene {len(color_secreto)} letras",
            f"Pista 3: Es {'primario' if color_secreto in colores_primarios else 'secundario'}"
        ]

        intentos_restantes = 3
        indice_pista = 0

        while intentos_restantes > 0:
            print(pistas[indice_pista])
            respuesta = input("¿Cuál es tu respuesta?: ")

            if respuesta.lower() == color_secreto.lower():
                print("🎉 Correcto! Adivinaste el color.")
                break
            else:
                intentos_restantes -= 1
                indice_pista += 1
                if intentos_restantes > 0:
                    print("No es correcto, intenta otra vez.\n")

        if intentos_restantes == 0:
            print(f"😢 Perdiste. El color era {color_secreto}.")
    else:
        print("Está bien, gracias por jugar!")

# ---- SALIR ----
elif opcion == 0:
    print("👋 Saliendo del programa, ojala vuelvas pronto, Hasta luego!")

# ---- OPCIÓN INVÁLIDA ----
else:
    print("Opción no válida. Ejecutá el programa otra vez.")
