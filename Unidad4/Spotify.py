#En Spotify se realiza el Music Recap de la temporada, donde para cada usuario se calculan las estadísicas de lo que ha escuchado. Se desea programar el algoritmo para que se ingrese el nombre de la canción y luego la cantidad de minutos de escucha sobre la misma. Como no se sabe cuántas canciones escuchó, se ingresaran una a una hasta que apareza una entrada de 0 minutos de escucha, lo cual indica el final. Al finalizar debe informar:
#La canción que más escuchaste fué: (nombre de la cancion)
#Escuchaste esa canción por (tiempo) minutos
#El total de minutos escuchados en la temporada es de (total)
#Esta temporada escuchaste (cantidad) canciones
cont = 0
suma = 0
nombre_cancion = int(input("Ingre el nombre de la cancion:"))
minutos_de_la_cancion = int(input("Ingre los minutos de la cancion:"))
maximo = minutos_de_la_cancion
while minutos_de_la_cancion > 0:
    if minutos_de_la_cancion > maximo:
        maximo = minutos_de_la_cancion
        nombreMaximo = nombre
    suma += minutos
    cont += 1
    nombre = int(input)
    minutos = int(input)
print("Resumen de temporada")
print("La canción que más escuchaste fue:", nombreMaximo)
print("Escuchaste esa canción por", maximo, "minutos")
print("El total de minutos escuchados es:", suma)
print("Cantidad de canciones escuchadas:", cont)
