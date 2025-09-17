a = 0
c = 0
nombre = input("Ingrese el nombre de la canción ")
min = int(input("Ingrese los minutos de escucha: "))
max = 0
nomMax = ""
while min != 0:
    c += 1
    a += min
    if min > max:
        max = min
        nomMax = nombre
    nombre = input("Ingrese el nombre de la canción ")
    min = int(input("Ingrese los minutos de escucha "))
if c > 0:
    print("La canción que más escuchaste fue:", nomMax)
    print("Escuchaste esa canción por", max,"minutos")
    print("El total de minutos escuchados en la temporada es de", a)
    print("Esta temporada escuchaste", c, "canciones")
else:
    print("No esccuhaste ninguna canción esta temporada")
