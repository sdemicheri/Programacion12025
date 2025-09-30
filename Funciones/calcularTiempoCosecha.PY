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
    dias_germinacion = float(input("Ingrese los dias que tarda en germinar la semilla: "))
    dias_crecimiento = float(input("Ingrese los dias de crecimiento: "))
    dias_maduracion = float(input("Ingrese los dias de maduracion hasta cosecha: "))
    total_de_dias = calcularTiempoCosecha(dias_germinacion,dias_crecimiento,dias_maduracion)
    print("el tiempo total en días desde que se planta hasta que se puede cosechar es:",total_de_dias)
