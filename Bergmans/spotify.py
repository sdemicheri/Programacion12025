cancion_mas_escuchada = ""
minutos_mas_escuchados = 0
total_minutos = 0
total_canciones = 0
nombre_cancion = input("Ingresa el nombre de la canción: ")
minutos_escucha = int(input("Ingresa la cantidad de minutos de escucha:"))

while minutos_escucha != 0:
    
    total_minutos += minutos_escucha
    total_canciones += 1

    if minutos_escucha > minutos_mas_escuchados:
        minutos_mas_escuchados = minutos_escucha
        cancion_mas_escuchada = nombre_cancion
    nombre_cancion = input("Ingresa el nombre de la canción: ")
    minutos_escucha = int(input("Ingresa la cantidad de minutos de escucha :"))

if total_canciones > 0:
    print("La canción que más escuchaste fue:", cancion_mas_escuchada)
    print("Escuchaste esa canción por", minutos_mas_escuchados, "minutos")
    print("El total de minutos escuchados en la temporada es de", total_minutos)
    print("Esta temporada escuchaste", total_canciones, "canciones")
else:
    print("No se ingresaron canciones en tu resumen.")
