print("-"*20)
print("  MENÚ DE JUEGOS  ")
print("-"*20)
print("\n")
print("1. Verdadero o Falso - Argentina")
print("2. Adivina el Número")
print("3. Piedra Papel o Tijera - Computadora")
print("\n")
opcion_elegida = input("Elige un juego (ingresa el número) o '0' para salir: ")
if opcion_elegida == "1":
    print(f"¡Elegiste Verdadero o Falso - Argentina!")
elif opcion_elegida == "2":
    print(f"!Elegiste Adivina el número!")
elif opcion_elegida == "3":
    print(f"¡Elegiste Piedra Papel o Tijera!")
elif opcion_elegida == "0":
    print(f"Fin del programa")
else:
    print(f"Opcion no valida, por favor ingrese un numero del 1 al 3 o 0 para finalizar el programa")
if opcion_elegida == "3":
    USUARIO = int(input("Eliga una jugada (ingrese el número) 1. Piedra 2. Papel 3. Tijera : "))
    if USUARIO == 1:
        jugada1 = "piedra"
    elif USUARIO == 2:
        jugada1 = "papel"
    elif USUARIO == 3:
        jugada1 = "tijera"
    import random
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

