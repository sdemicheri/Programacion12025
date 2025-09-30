"""
En Spotify se realiza el Music Recap de la temporada, 
donde para cada usuario se calculan las estadísticas de lo que ha escuchado. 
Se desea programar el algoritmo para que se ingrese el nombre de la canción y 
luego la cantidad de minutos de escucha sobre la misma. 
Como no se sabe cuántas canciones escuchó, 
se ingresaran una a una hasta que aparezca una entrada de 0 minutos de escucha, 
lo cual indica el final. Al finalizar debe informar:

La canción que más escuchaste fué: (nombre de la canción)
Escuchaste esa canción por (tiempo) minutos
El total de minutos escuchados en la temporada es de (total)
Esta temporada escuchaste (cantidad) canciones
"""
minutos = int(input("Ingrese los minutos escuchados de la canción: "))
nombre_cancion = input("Ingrese el nombre de la canción: ")

contador_canc = 0
suma_min = minutos
mayor_min = minutos
mayor_nombre = nombre_cancion

while minutos != 0:
    minutos = int(input("Ingrese los minutos escuchados de la canción: "))
    if minutos != 0:
        nombre_cancion = input("Ingrese el nombre de la canción: ")
    suma_min += minutos
    contador_canc += 1
    
    if minutos > mayor_min:
        mayor_min = minutos
        mayor_nombre = nombre_cancion

print(f"La canción que más escuchaste fué: {mayor_nombre}")
print(f"Escuchaste esa canción por {mayor_min} minutos")
print(f"El total de minutos escuchados en la temporada es de {suma_min}")
print(f"Esta temporada escuchaste {contador_canc} canciones")