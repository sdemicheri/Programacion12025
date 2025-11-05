"""
Una empresa dedicada a la venta de productos electrónicos necesita analizar el comportamiento de sus ventas 
durante el último año. Para ello, el área de administración registrará, mediante un sistema, 
cada operación realizada indicando el mes de la venta y el importe total correspondiente.
El proceso de carga finalizará cuando se ingrese el mes 0, 
indicando que no hay más registros para procesar.
El objetivo es obtener un informe que muestre la cantidad de ventas por cada mes 
y determinar cuál fue el mes con el mayor importe total de ventas.
"""
vector_meses = [0]*13
vector_importes = [0]*13

mes = int(input())
while mes > 0:
    vector_meses[mes] += 1
    importe = int(input())
    vector_importes[mes] += importe
    mes = int(input())

for i in range(len(vector_meses)):
    if vector_meses[i] > 0:
        print(f"Mes: {i}")
        print(f"Ventas: {vector_meses[i]}")

mayor_importe = vector_importes[1]
posiciondelMayor = 1
for i in range(len(vector_importes)):
    if vector_importes[i] > mayor_importe:
        mayor_importe = vector_importes[i]
        posiciondelMayor = i

print(f"Mayor importe de venta, Mes {posiciondelMayor}")    