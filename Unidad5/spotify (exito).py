can_Y = int(input("ingrese un numero para comenzar:"))
cont = 0
acu = 0
max_t = 0
nom_max = 0
while( can_Y != 0):
    can_X = input("ingrese el nombre de la cancion: ")
    cont += 1
    can_Y = int(input("ingrese la cantidad de minutos que dura la cacnion: "))
    acu = can_Y + acu
    if( can_Y > max_t ):
        max_t = can_Y
        nom_max = can_X

print("La cancion que mas escuchas fue:", nom_max)
print("Escuchaste esta cancion por:", acu)
print("El total de minutos escuchados en la temporad es de:", max_t)
print("El total de canciones que escuchaste fue:", cont)