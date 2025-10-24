vector = [0] * 10
suma = 0
contador = 0

for i in range(10):
    vector[i] = int(input("Ingrese su edad: "))
    suma += vector[i]

promedio = suma/10

for i in range(10):
    if vector[i] > promedio:
        contador += 1

print("Promedio General:",promedio)
print("Cantidad de Edades mayores al promedio:",contador)