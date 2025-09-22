import random

print("Bienvenido al juego de Cara o Cruz!")

while True:  # bucle principal
    respuesta_inicio = input("¿Estás listo para jugar? (si/no): ")

    if respuesta_inicio == "si":
        # El jugador elige
        eleccion = input("Elegí: cara o cruz: ")

        # La computadora lanza la moneda
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
