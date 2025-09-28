total_minutos = 0
cantidad_canciones = 0
cancion_mas_escuchada = ""
max_minutos = -1   # arranca con un valor muy bajo

for cancion in range (3): #conteo de preguntas y de canciones a calcular
    cancion = input("Ingrese el nombre de la canción: ")
    minutos = int(input("Ingrese los minutos de escucha (0 para terminar): "))

    if minutos == 0:   # condición de corte
        break

    total_minutos += minutos
    cantidad_canciones += 1

    # Verificar la mas escuchada
    if minutos > max_minutos:
        max_minutos = minutos
        cancion_mas_escuchada = cancion

# Al salir del bucle mostrar resultados
print("\nLa canción que más escuchaste fue:", cancion_mas_escuchada)
print("Escuchaste esa canción por", max_minutos, "minutos")
print("El total de minutos escuchados en la temporada es de", total_minutos)
print("Esta temporada escuchaste", cantidad_canciones, "canciones")