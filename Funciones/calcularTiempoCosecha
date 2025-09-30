"""
Función 8: calcularTiempoCosecha(dias_germinacion, dias_crecimiento, dias_maduracion)
Descripción: Calcula el tiempo total en días desde que se planta hasta que se puede cosechar, sumando las tres etapas del ciclo de vida de la planta.
Entrada:
dias_germinacion: número decimal con los días que tarda en germinar la semilla
dias_crecimiento: número decimal con los días de crecimiento
dias_maduracion: número decimal con los días de maduración hasta cosecha
Salida:
Retorna un número decimal con el total de días
Lógica requerida:
Sumar los tres valores
"""
def calcularTiempoCosecha(dias_germinacion,dias_crecimiento,dias_maduracion):
    return dias_germinacion + dias_crecimiento + dias_maduracion

if __name__ == "__main__":
    dias_germinacion = float(input("Días de germinación (semilla a brote): "))
    dias_crecimiento = float(input("Días de crecimiento (brote a planta adulta): "))
    dias_maduracion = float(input("Días de maduración (hasta cosecha): "))
    dias_totales = calcularTiempoCosecha(dias_germinacion,dias_crecimiento,dias_maduracion)

    print(f"\n✓ Tiempo total hasta cosecha: {int(dias_totales)} días")