# PIEDRA, PAPEL O TIJERA
print("------------------------")
print("Bienvenidos a Piedra, Papel o Tijera ")
print("Opciones: ")
print("1 Piedra")
print("2 Papel")
print("3 Tijera")
print("------------------------")
try:
    ganador = False
    while not ganador:
        jugador1= int(input("Jugador 1, elige tu opción (1-3): "))
        jugador2= int(input("Jugador 2, elige tu opción (1-3): "))
        if jugador1 == jugador2:
         print("Empate, jueguen de nuevo ")
        elif jugador1 == 1 and jugador2 == 3 or jugador1 == 2 and jugador2 == 1 or jugador1 == 3 and jugador2 == 2:
         print("Jugador 1 gana ")
         ganador = True
        else:
            print("Jugador 2 gana ")
            ganador = True
except ValueError:
    print("Ingresó un dato no válido. Por favor, intente de nuevo ")
