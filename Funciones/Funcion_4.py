"""
Función 4: calcularSemillas(cantidad_plantas, semillas_por_planta)

Descripción: Calcula el total de semillas necesarias. Se plantan varias semillas por planta porque algunas pueden no germinar.
Entrada:
cantidad_plantas: número entero con la cantidad de plantas a cultivar
semillas_por_planta: número decimal con cuántas semillas plantar por cada planta

Salida:
Retorna un número decimal con el total de semillas necesarias
Lógica requerida:
Multiplicar cantidad de plantas por semillas por planta
"""

def calcularSemillas(cantidad_plantas, semillas_por_planta):

    total_Semillas = cantidad_plantas * semillas_por_planta

    return float(total_Semillas)


cantidad_plantas = int(input("Ingrese cantidad de plantas: "))
semillas_por_planta = float(input("Ingrese cantidad de semillas por planta: "))

total_semillas = calcularSemillas(cantidad_plantas, semillas_por_planta)

print("Total de semillas necesarias:", total_semillas)