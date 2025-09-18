temporada = 90
cont = 0
acu = 1
while( temporada == 90):
    can_X = input("ingrese el nombre de la cancion(si ya no escucho mas canciones escriba TERMINADO):")
    if( can_X == "TERMINADO"):
        break
    cont += 1
    can_Y = int(input("ingrese la cantidad de minutos que dura la cacion:"))
    acu = can_Y + acu

print(acu)
