edad = [0]*11
acu = 0
for i in range(11):
    edad[i] = int(input())
    acu = acu + edad[i]
promedio = acu / 11
for i in range(11):
    if edad[i] > promedio:
        print(f"alumno {i} sos mayor al promedio, tenés {edad[i]}")
        
"---------"

edad = [0]*10
acu = 0
mayorPromedio = 0
for i in range(10):
    edad[i] = int(input())
    acu = acu + edad[i]
promedio = acu / 10
print("Promedio General:", promedio)
for i in range(10):
    if edad[i] > promedio:
        mayorPromedio += 1
print("Cantidad de Edades mayores al promedio:", mayorPromedio)