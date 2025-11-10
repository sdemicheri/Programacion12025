ventasMes = [0] * 12
cantidad = [0] * 12

while True:
    mes = int(input("Mes (1-12, 0 para terminar): "))
    if mes == 0:
        break
    else:
        monto = float(input("Importe de la venta: "))
        ventasMes[mes - 1] += monto
        cantidad[mes - 1] += 1

for i in range(12):
    if cantidad[i] > 0:
        print("Mes", i + 1, "- Cantidad de ventas:", cantidad[i], "- Total vendido:", ventasMes[i])

mayor = ventasMes[0]
mesMayor = 1
for i in range(12):
    if ventasMes[i] > mayor:
        mayor = ventasMes[i]
        mesMayor = i + 1

print("\nEl mes con mayor importe total de ventas fue:", mesMayor)