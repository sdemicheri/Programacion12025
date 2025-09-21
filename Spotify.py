cancionesTotales = 0
minutosTotales = 0
cancionME = ""
minutosMax = 0

cancion = input("Ingrese la canción (enter para finalizar): ")
while cancion != "":
    minutos = float(input("Ingrese la cantidad de minutos: "))
    minutosTotales += minutos
    cancionesTotales += 1
    if minutos > minutosMax:
        minutosMax = minutos
        cancionME = cancion
    cancion = input("Ingrese la canción (enter para finalizar): ")

print("La canción que más escuchaste fue:", cancionME)
print("Escuchaste esa canción por", minutosMax, "minutos")
print("El total de minutos escuchados en la temporada es de", minutosTotales)
print("Esta temporada escuchaste", cancionesTotales, "canciones")