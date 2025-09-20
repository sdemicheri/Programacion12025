import random
print("-"*18)
print("  MENÚ DE JUEGOS  ")
print("-"*18)
print("")
print("1. Trivia - Argentina")
print("2. Adivina el Número")
print("3. Piedra Papel o Tijera - Computadora")
print("")
opcion_elegida = input("Elige un juego (ingresa el número) o '0' para salir: ")
print("")
if opcion_elegida == "1":
    print("-"*46)
    print("Iniciando: 'Trivia - Argentina' ¡Buena suerte!")
    print("-"*46)
elif opcion_elegida == "2":
    print("-"*45)
    print("Iniciando: 'Adivina el número' ¡Buena suerte!")
    print("-"*45)
elif opcion_elegida == "3":
    print("-"*49)
    print("Iniciando: 'Piedra Papel o Tijera' ¡Buena suerte!")
    print("-"*49)
elif opcion_elegida == "0":
    print(f"FINALIZANDO EL PROGRAMA...")
else:
    print(f"Opcion no valida, por favor revise la entrada")
if opcion_elegida == "3":
    USUARIO = int(input("Eliga una jugada (ingrese el número) 1. Piedra 2. Papel 3. Tijera : "))
    if USUARIO == 1:
        jugada1 = "piedra"
    elif USUARIO == 2:
        jugada1 = "papel"
    elif USUARIO == 3:
        jugada1 = "tijera"
    computadora = random.randint(1,3)
    if computadora == 1:
        jugada2 = "piedra"
    elif computadora == 2:
        jugada2 = "papel"
    elif computadora == 3:
        jugada2 = "tijera"
    if (jugada1 == "piedra" or jugada1 == "papel" or jugada1 == "tijera") \
        and (jugada2 == "piedra" or jugada2 == "papel" or jugada2 == "tijera"):
        if jugada1 == jugada2:
            print(f"EMPATE, ambos eligieron {jugada1}")
        elif (jugada1 == "piedra" and jugada2 == "tijera") or \
            (jugada1 == "papel" and jugada2 == "piedra") or \
            (jugada1 == "tijera" and jugada2 == "papel"):
            print(f"GANA {"USUARIO"} con {jugada1} contra {"computadora"} con {jugada2}")
        else:
            print(f"GANA {"COMPUTADORA"} con {jugada2} contra {"USUARIO"} con {jugada1}")
    else:
        print("Los datos ingresados en las jugadas no son validos")

elif opcion_elegida == "2":
    pc_nro = random.randint(1,10)
    intentos = 3
    ganaste = False
    while intentos > 0 and not ganaste:
            if intentos == 1:
                numero = int(input(f"Te queda {intentos} intento, Ingresa tu número del 1 al 10: "))
            elif intentos == 2 or intentos == 3:
                numero = int(input(f"Te quedan {intentos} intentos, Ingresa tu número del 1 al 10: "))
            if pc_nro == numero:
                if intentos == 3:
                    print("¡A LA PRIMERA ADIVINASTE!, LOCURAAAA")
                else:
                    print("¡ADIVINASTE GENI@, FELICITACIONES!")
                ganaste = True
            else:
                intentos -= 1
    print("Perdiste pero no pasa nada rey")