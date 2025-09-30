def calcularAguaMensual(agua_diaria, dias_mes):
    return agua_diaria * dias_mes


consumo_mensual = calcularAguaMensual(2.4, 30)
print(f"Consumo mensual: {consumo_mensual} litros")