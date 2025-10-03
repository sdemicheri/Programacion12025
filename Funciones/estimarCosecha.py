#Función 7: estimarCosecha(cantidad_plantas, kilos_por_planta, porcentaje_exito)
#Descripción: Estima la cosecha real considerando que no todas las plantas producirán exitosamente. Calcula primero la cosecha ideal y luego aplica el porcentaje de éxito.
#Entrada:
#cantidad_plantas: número entero con la cantidad de plantas
#kilos_por_planta: número decimal con los kilos que produce cada planta
#porcentaje_exito: número decimal entre 0 y 100 (ejemplo: 80 significa 80%)
#Salida:
#Retorna un número decimal con los kilos estimados de cosecha
#Lógica requerida:
#Calcular cosecha ideal: cantidad_plantas × kilos_por_planta
#Calcular cosecha real: cosecha_ideal × (porcentaje_exito / 100)

def estimarCosecha(cantidad_plantas, kilos_por_planta, porcentaje_exito):
    cosecha_ideal=cantidad_plantas*kilos_por_planta
    cosecha_real=cosecha_ideal*(porcentaje_exito/100)
    return cosecha_real

kilos_estimados_de_cosecha=estimarCosecha(100, 19.9, 28.0)
print(kilos_estimados_de_cosecha)




