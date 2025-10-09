reporte = input()
reporteB = ""

for i in range(len(reporte)):
    if reporte[i] == ",":
        reporteB += "."
    elif reporte[i] != ",":
        reporteB += reporte[i]

contador = 0
for i in range(len(reporteB)-1, -1):
    if reporteB[i] == ".":
        contador += 1
    while contador == 1:
        reporteB[i] == ","

print(reporteB)