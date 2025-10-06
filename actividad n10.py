def calcularFertilizante(cantidadplantas, gramosporplanta, aplicaciones):


    fertilizanteporaplicacion = cantidadplantas * gramosporplanta
    total = fertilizanteporaplicacion * aplicaciones
    return total


cantidad = int(input("Ingrese la cantidad de plantas: "))
gramos = float(input("Ingrese los gramos por planta: "))
veces = int(input("Ingrese la cantidad de aplicaciones: "))
total = calcularFertilizante(cantidad, gramos, veces)

print(f"Se necesitan {total:.2f} gramos de fertilizante en total")