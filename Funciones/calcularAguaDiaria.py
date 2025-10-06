#Función 5: #calcularAguaDiaria(cantidad_plantas, litros_por_planta)
#Descripción: Calcula cuántos litros de agua se necesitan diariamente para regar todas las plantas.
#Entrada:
#cantidad_plantas: número entero con la cantidad de plantas
#litros_por_planta: número decimal con los litros que necesita cada planta por día
#Salida:
#Retorna un número decimal con los litros diarios totales
#Lógica requerida:
#Multiplicar cantidad de plantas por litros por planta

#FORMA N°1
def calcularAguaDiaria (cantidad_plantas , litros_por_plantas):
    return cantidad_plantas * litros_por_plantas

if __name__ == "__main__":
    cantidad_plantas = int(input("Ingrese cantidad de plantas: "))
    litros_por_plantas = float(input("Ingrese los litros que necesita cada planta por día: "))
    agua_diaria = calcularAguaDiaria(cantidad_plantas , litros_por_plantas)
    
    print(f"\n✓ Necesitarán regar con {agua_diaria:.2f} litros diarios")