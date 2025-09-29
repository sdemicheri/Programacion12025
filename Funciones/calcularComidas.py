"""
Función 4: calcularComidas()

Responsable: Estudiante D
Descripción: Calcula el gasto en comidas.
Entrada: Cantidad de personas, días de viaje, presupuesto diario por persona
Salida: Retorna el costo total en comidas
Lógica: Multiplicar personas × días × presupuesto diario.
"""
def calcularComidas(cantidad_personas, dias, presupuesto_diario):
    return cantidad_personas * dias * presupuesto_diario

if __name__ == "__main__":
    cantidad_personas = int(input("Ingrese la cantidad de personas: "))
    dias = int(input("Ingrese la cantidad de días del viaje: "))
    presupuesto_diario = int(input("Ingrese el presupuesto diario por persona para comidas: "))    
    costo_comida = calcularComidas(cantidad_personas, dias, presupuesto_diario)

    print("el costo total es: ",costo_comida)