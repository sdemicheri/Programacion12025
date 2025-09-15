"""
ENTRADA:
Temperatura diaria

PROCESO:
Pedir temp el lunes, martes, miércoles, jueves, viernes, sábado y domingo
Calcular promedio 

SALIDA:
Promedio
"""
suma = 0
for i in range (7):
    temp = float(input("Ingrese la temperatura de hoy: "))
    suma += temp

promedio = (suma)/7

print(f"El promedio de la temperatura semanal es: {promedio:.2f}")