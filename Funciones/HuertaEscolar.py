# ============================================================================
# ENUNCIADO PARA TAREA - FECHA DE ENTREGA 06/10/2025
# ============================================================================
"""
Planificación de Huerta Escolar

La escuela está implementando un proyecto de huerta sustentable y necesita un sistema que ayude a planificar todos los aspectos: 
dimensiones, recursos necesarios, cronograma de trabajo y proyección de cosecha.
Cada estudiante debe desarrollar UNA función específica que será integrada en el sistema completo.
Es fundamental respetar exactamente las especificaciones de entrada y salida de cada función para que la integración sea exitosa.

Funcionalidades a Implementar

Función 1: validarPositivo()
Descripción: Solicita al usuario que ingrese un número y valida que sea mayor a 0. Si el usuario ingresa un valor inválido (0 o negativo), debe mostrar un mensaje de error y volver a solicitar el número.
Entrada: Ninguna (solicita datos por teclado dentro de la función)

Salida: Retorna un número decimal (float) mayor a 0

Lógica requerida: Usar estructura repetitiva (while)
Continuar pidiendo el número hasta que sea válido

Función 2: calcularAreaDisponible(largo, ancho)
Descripción: Calcula el área total del terreno disponible para la huerta en metros cuadrados.
Entrada:
largo: número decimal que representa el largo del terreno en metros
ancho: número decimal que representa el ancho del terreno en metros

Salida:
Retorna un número decimal con el área total en m²

Lógica requerida:
Multiplicar largo por ancho

Función 3: calcularCantidadPlantas(area_total, espacio_por_planta)
Descripción: Calcula cuántas plantas caben en el área disponible, considerando el espacio que ocupa cada planta.
Entrada:
area_total: número decimal con el área disponible en m²
espacio_por_planta: número decimal con el espacio que necesita cada planta en m²
Salida:
Retorna un número entero con la cantidad de plantas que caben (redondear hacia abajo)
Lógica requerida:
Dividir área total entre espacio por planta
Convertir el resultado a entero (descartar decimales)

Función 4: calcularSemillas(cantidad_plantas, semillas_por_planta)

Descripción: Calcula el total de semillas necesarias. Se plantan varias semillas por planta porque algunas pueden no germinar.
Entrada:
cantidad_plantas: número entero con la cantidad de plantas a cultivar
semillas_por_planta: número decimal con cuántas semillas plantar por cada planta

Salida:
Retorna un número decimal con el total de semillas necesarias
Lógica requerida:
Multiplicar cantidad de plantas por semillas por planta

Función 5: calcularAguaDiaria(cantidad_plantas, litros_por_planta)
Descripción: Calcula cuántos litros de agua se necesitan diariamente para regar todas las plantas.
Entrada:
cantidad_plantas: número entero con la cantidad de plantas
litros_por_planta: número decimal con los litros que necesita cada planta por día
Salida:
Retorna un número decimal con los litros diarios totales
Lógica requerida:
Multiplicar cantidad de plantas por litros por planta

Función 6: calcularAguaMensual(agua_diaria, dias_mes)
Descripción: Calcula el consumo total de agua en un mes.
Entrada:
agua_diaria: número decimal con los litros diarios necesarios
dias_mes: número entero con la cantidad de días del mes (28, 30 o 31)

Salida:
Retorna un número decimal con los litros mensuales totales

Lógica requerida:
Multiplicar agua diaria por días del mes

Función 7: estimarCosecha(cantidad_plantas, kilos_por_planta, porcentaje_exito)
Descripción: Estima la cosecha real considerando que no todas las plantas producirán exitosamente. Calcula primero la cosecha ideal y luego aplica el porcentaje de éxito.
Entrada:
cantidad_plantas: número entero con la cantidad de plantas
kilos_por_planta: número decimal con los kilos que produce cada planta
porcentaje_exito: número decimal entre 0 y 100 (ejemplo: 80 significa 80%)
Salida:
Retorna un número decimal con los kilos estimados de cosecha
Lógica requerida:
Calcular cosecha ideal: cantidad_plantas × kilos_por_planta
Calcular cosecha real: cosecha_ideal × (porcentaje_exito / 100)

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

Función 9: determinarEficiencia(area_usada, area_total)
Descripción: Determina qué tan eficiente es el uso del espacio disponible y retorna un mensaje evaluativo según el porcentaje de aprovechamiento.
Entrada:
area_usada: número decimal con el área realmente utilizada en m²
area_total: número decimal con el área total disponible en m²
Salida:
Retorna un texto (string) con el mensaje de evaluación
Lógica requerida:
Calcular porcentaje: (area_usada / area_total) × 100
Usar estructura condicional:
Si porcentaje >= 90: retornar "EXCELENTE - Aprovechamiento óptimo del espacio"
Si porcentaje >= 70: retornar "BUENO - Buen uso del espacio disponible"
Si porcentaje >= 50: retornar "REGULAR - Se puede mejorar la distribución"
Si no: retornar "BAJO - Hay mucho espacio sin utilizar"

Función 10: calcularFertilizante(cantidad_plantas, gramos_por_planta, aplicaciones)
Descripción: Calcula la cantidad total de fertilizante necesario durante todo el ciclo de cultivo, considerando que se aplicará varias veces.
Entrada:
cantidad_plantas: número entero con la cantidad de plantas
gramos_por_planta: número decimal con los gramos que necesita cada planta por aplicación
aplicaciones: número entero con cuántas veces se aplicará fertilizante
Salida:
Retorna un número decimal con el total de gramos de fertilizante
Lógica requerida:
Calcular fertilizante por aplicación: cantidad_plantas × gramos_por_planta
Calcular total: fertilizante_por_aplicacion × aplicaciones

Función 11: calcularCercado(largo, ancho)
Descripción: Calcula el perímetro del terreno para saber cuántos metros lineales de cerco se necesitan para proteger la huerta.
Entrada:
largo: número decimal con el largo del terreno en metros
ancho: número decimal con el ancho del terreno en metros
Salida:
Retorna un número decimal con el perímetro en metros
Lógica requerida:
Calcular perímetro: 2 × (largo + ancho)

Función 12: determinarEstacion(mes)
Descripción: Determina en qué estación del año se encuentra según el mes ingresado y proporciona una recomendación de qué plantar en esa época.
Entrada:
mes: número entero del 1 al 12 (1=enero, 2=febrero, etc.)
Salida:
Retorna un texto (string) con la estación y recomendación
Lógica requerida:
Usar estructura condicional múltiple:
Si mes = 12, 1 o 2: retornar "VERANO - Ideal para tomates, pimientos y berenjenas"
Si mes = 3, 4 o 5: retornar "OTOÑO - Ideal para lechugas, espinacas y acelgas"
Si mes = 6, 7 o 8: retornar "INVIERNO - Ideal para brócoli, coliflor y repollo"
Si mes = 9, 10 o 11: retornar "PRIMAVERA - Ideal para zanahoria, remolacha y rábanos"

Función 13: calcularCompostNecesario(area_total, kilos_por_m2)
Descripción: Calcula cuánto compost (abono orgánico) se necesita para preparar el suelo antes de plantar.
Entrada:
area_total: número decimal con el área total del terreno en m²
kilos_por_m2: número decimal con los kilos de compost necesarios por cada m²
Salida:
Retorna un número decimal con el total de kilos de compost
Lógica requerida:
Multiplicar área total por kilos por m²

Función 14: calcularHorasTrabajo(cantidad_plantas, minutos_por_planta)
Descripción: Calcula cuántas horas de trabajo se necesitan para plantar todas las plantas, considerando el tiempo que toma plantar cada una.
Entrada:
cantidad_plantas: número entero con la cantidad de plantas
minutos_por_planta: número decimal con los minutos que toma plantar cada una
Salida:
Retorna un número decimal con el total de horas
Lógica requerida:
Calcular minutos totales: cantidad_plantas × minutos_por_planta
Convertir a horas: minutos_totales / 60

Función 15: mostrarPlanHuerta(...)
Descripción: Muestra en pantalla un reporte completo y formateado con toda la información del plan de huerta.
Entrada:
area_total: número decimal con área total en m²
cantidad_plantas: número entero de plantas
area_usada: número decimal con área utilizada en m²
semillas: número decimal con total de semillas
agua_diaria: número decimal con litros diarios
agua_mensual: número decimal con litros mensuales
cosecha_estimada: número decimal con kg estimados
dias_cosecha: número decimal con días hasta cosechar
eficiencia: texto con el mensaje de eficiencia
fertilizante: número decimal con gramos totales
cercado: número decimal con metros de cerco
estacion: texto con estación y recomendación
compost: número decimal con kg de compost
horas_trabajo: número decimal con horas de plantación
Salida:
No retorna nada (imprime en pantalla usando print())
Lógica requerida:
Estructura secuencial de múltiples print()
Formatear números con 2 decimales usando .2f
Organizar información en secciones claras

"""
# ============================================================================
# EXPORTAR FUNCIONES EXTERNAS
# ============================================================================

#import
import calcularTiempoCosecha

# ============================================================================
# FUNCIONES
# ============================================================================

def validarPositivo():
    try:
        valor = float(input())
        while valor <= 0:
            print("Ingresó un dato no válido, intente nuevamente")
            valor = float(input())
        return valor
    except ValueError:
        print("Ingresó un dato no válido")
        return 0   
    
def calcularAguaMensual(agua_diaria, dias_mes):
    return agua_diaria * dias_mes   


# ============================================================================
# FUNCION DEL PROGRAMA PRINCIPAL
# ============================================================================

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                    HUERTA ESCOLAR                        ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    print("Ingrese el largo del terreno (en metros):")
    largo = validarPositivo()
    
    print("Ingrese el ancho del terreno (en metros):")
    ancho = validarPositivo()
    
    area_total = calcularAreaDisponible(largo, ancho)
    print(f"\n✓ Área total disponible: {area_total:.2f} metros cuadrados")
    
    print("¿Cuánto espacio necesita cada planta? (en m²)")
    print("Ejemplos: Tomate=0.5, Lechuga=0.25, Zanahoria=0.1")
    espacio_por_planta = validarPositivo()
    
    cantidad_plantas = calcularCantidadPlantas(area_total, espacio_por_planta)
    print(f"\n✓ Pueden plantar {cantidad_plantas} plantas en este espacio")
    
    print("¿Cuántas semillas se plantan por cada planta?")
    print("(Se plantan extras por si algunas no germinan)")
    semillas_por_planta = validarPositivo()
    
    total_semillas = calcularSemillas(cantidad_plantas, semillas_por_planta)
    print(f"\n✓ Necesitarán {int(total_semillas)} semillas en total")
    
    print("¿Cuántos litros de agua necesita cada planta por día?")
    litros_por_planta = validarPositivo()
    
    agua_diaria = calcularAguaDiaria(cantidad_plantas, litros_por_planta)
    print(f"\n✓ Necesitarán regar con {agua_diaria:.2f} litros diarios")
    
    print("\nIngrese la cantidad de días del mes (28, 30 o 31):")
    dias_mes = int(validarPositivo())
    
    agua_mensual = calcularAguaMensual(agua_diaria, dias_mes)
    print(f"\n✓ Consumo mensual de agua: {agua_mensual:.2f} litros")
    
    print("¿Cuántos kilos produce cada planta en promedio?")
    kilos_por_planta = validarPositivo()
    
    print("¿Qué porcentaje de éxito esperan? (ej: 80 para 80%)")
    porcentaje_exito = validarPositivo()
    
    while porcentaje_exito > 100:
        print("El porcentaje no puede ser mayor a 100. Intente nuevamente:")
        porcentaje_exito = validarPositivo()
    
    cosecha_estimada = estimarCosecha(cantidad_plantas, kilos_por_planta, porcentaje_exito)
    print(f"\n✓ Cosecha estimada: {cosecha_estimada:.2f} kilogramos")

    print("Días de germinación (semilla a brote):")
    dias_germinacion = validarPositivo()
    
    print("Días de crecimiento (brote a planta adulta):")
    dias_crecimiento = validarPositivo()
    
    print("Días de maduración (hasta cosecha):")
    dias_maduracion = validarPositivo()
    
    dias_totales = calcularTiempoCosecha.calcularTiempoCosecha(dias_germinacion, dias_crecimiento, dias_maduracion)
    print(f"\n✓ Tiempo total hasta cosecha: {int(dias_totales)} días")

    area_utilizada = cantidad_plantas * espacio_por_planta
    
    mensaje_eficiencia = determinarEficiencia(area_utilizada, area_total)
    
    print("¿Cuántos gramos de fertilizante necesita cada planta?")
    gramos_por_planta = validarPositivo()
    
    print("¿Cuántas veces aplicarán fertilizante durante el ciclo?")
    aplicaciones = int(validarPositivo())
    
    total_fertilizante = calcularFertilizante(cantidad_plantas, gramos_por_planta, aplicaciones)
    print(f"\n✓ Fertilizante total necesario: {total_fertilizante:.2f} gramos")
    
    perimetro_cercar = calcularCercado(largo, ancho)
    print(f"\n✓ Necesitarán {perimetro_cercar:.2f} metros de cerco")
    
    print("¿En qué mes van a plantar? (1-12)")
    mes = int(validarPositivo())
    
    while mes < 1 or mes > 12:
        print("Mes inválido. Debe ser entre 1 y 12:")
        mes = int(validarPositivo())
    
    info_estacion = determinarEstacion(mes)
    print(f"\n✓ {info_estacion}")
    
    print("¿Cuántos kilos de compost por m² necesitan?")
    print("(Recomendado: 3-5 kg/m²)")
    kilos_compost_m2 = validarPositivo()
    
    total_compost = calcularCompostNecesario(area_total, kilos_compost_m2)
    print(f"\n✓ Compost necesario: {total_compost:.2f} kg")

    print("¿Cuántos minutos toma plantar cada planta?")
    minutos_por_planta = validarPositivo()
    
    horas_plantacion = calcularHorasTrabajo(cantidad_plantas, minutos_por_planta)
    print(f"\n✓ Tiempo total de plantación: {horas_plantacion:.2f} horas")
    
    mostrarPlanHuerta(area_total, cantidad_plantas, area_utilizada, total_semillas, 
                      agua_diaria, agua_mensual, cosecha_estimada, dias_totales, mensaje_eficiencia,
                      total_fertilizante, perimetro_cercar, info_estacion, total_compost, horas_plantacion)
    
    print("¡Plan de huerta generado exitosamente! 🌿🥬🍅")


# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()