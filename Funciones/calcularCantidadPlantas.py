import math
def calcularCantidadPlantas(area_total, espacio_por_planta):
    resultado = area_total / espacio_por_planta
    return math.floor(resultado)
