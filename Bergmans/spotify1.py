
cancion_mas_escuchada = ""
tiempo_maximo = 0
total_minutos = 0
cantidad_canciones = 0




nombre_cancion = input("Introduce el nombre de la canción: ")
try:
    minutos_escucha = float(input(f"Introduce los minutos de escucha de '{nombre_cancion}': "))
except ValueError:
    minutos_escucha = -1  


while minutos_escucha > 0:
    
    if minutos_escucha > tiempo_maximo:
        tiempo_maximo = minutos_escucha
        cancion_mas_escuchada = nombre_cancion
    
    total_minutos += minutos_escucha
    cantidad_canciones += 1
    
   
    nombre_cancion = input("Introduce el nombre de la siguiente canción: ")
    try:
        minutos_escucha = float(input(f"Introduce los minutos de escucha de '{nombre_cancion}': "))
    except ValueError:
        minutos_escucha = -1 



if cantidad_canciones > 0:
    print(f"La canción que más escuchaste fue: {cancion_mas_escuchada}")
    print(f"Escuchaste esa canción por {tiempo_maximo} minutos")
    print(f"El total de minutos escuchados en la temporada es de {total_minutos}")
    print(f"Esta temporada escuchaste {cantidad_canciones} canciones")
else:
    print("No se ingresaron canciones para el resumen.")