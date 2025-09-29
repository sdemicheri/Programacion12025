# ============================================================================
# ENUNCIADO PARA TRABAJAR EN CLASE 29/09/2025
# ============================================================================
'''
Un grupo de amigos quiere hacer un viaje y necesitan calcular cuánto debe pagar cada uno. 
Deben considerar: combustible, peajes, comidas y alojamiento. 
Cada persona del grupo implementará una función diferente y luego las combinaremos en un programa principal.
Funcionalidades a Implementar

Cada estudiante debe implementar UNA de las siguientes funciones:

Función 1: validarPositivo()

Responsable: Estudiante A
Descripción: Solicita un número y valida que sea mayor a 0.
Entrada: Ninguna (solicita datos por teclado)
Salida: Retorna el número válido ingresado
Lógica: Usar estructura repetitiva (while o do-while) para seguir pidiendo el número hasta que sea mayor a 0.

Función 2: calcularCombustible()

Responsable: Estudiante B
Descripción: Calcula el costo de combustible del viaje.
Entrada: Kilómetros a recorrer, consumo del auto (km/litro), precio por litro
Salida: Retorna el costo total de combustible
Lógica: Calcular litros necesarios y multiplicar por precio.

Función 3: calcularPeajes()

Responsable: Estudiante C
Descripción: Calcula el costo total de peajes.
Entrada: Cantidad de peajes a pasar
Salida: Retorna el costo total de peajes
Lógica: Usar estructura repetitiva para pedir el precio de cada peaje y sumarlos.

Función 4: calcularComidas()

Responsable: Estudiante D
Descripción: Calcula el gasto en comidas.
Entrada: Cantidad de personas, días de viaje, presupuesto diario por persona
Salida: Retorna el costo total en comidas
Lógica: Multiplicar personas × días × presupuesto diario.

Función 5: calcularAlojamiento()

Responsable: Estudiante E
Descripción: Calcula el costo de alojamiento.
Entrada: Cantidad de noches, precio por noche
Salida: Retorna el costo total de alojamiento
Lógica: Multiplicar noches por precio.

Función 6: dividirGastos()

Responsable: Estudiante F
Descripción: Divide el gasto total entre las personas.
Entrada: Gasto total, cantidad de personas
Salida: Retorna cuánto paga cada persona
Lógica: Dividir el total entre la cantidad de personas.

Función 7: aplicarDescuento()

Responsable: Estudiante G
Descripción: Aplica un descuento si el grupo es numeroso.
Entrada: Monto total, cantidad de personas
Salida: Retorna el monto con descuento aplicado
Lógica: Usar condicionales:

Si son 5 o más personas: 10% de descuento
Si son 3 o 4 personas: 5% de descuento
Si son menos de 3: sin descuento



Función 8: mostrarResumen()

Responsable: Estudiante H
Descripción: Muestra un resumen completo del viaje.
Entrada: Todos los costos calculados y el monto por persona
Salida: Imprime en pantalla un resumen formateado
Lógica: Estructura secuencial para mostrar todos los datos.


Programa Principal
1. Solicitar cantidad de personas (usando validarPositivo)
2. Solicitar datos del viaje (km, consumo, precio nafta) usando validarPositivo
3. Calcular costo de combustible con calcularCombustible()
4. Calcular costo de peajes con calcularPeajes()
5. Solicitar días de viaje y calcular comidas con calcularComidas()
6. Solicitar noches y calcular alojamiento con calcularAlojamiento()
7. Sumar todos los costos = TOTAL
8. Aplicar descuento con aplicarDescuento()
9. Dividir gastos con dividirGastos()
10. Mostrar resumen con mostrarResumen()
'''
# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    print("╔════════════════════════════════════════════════╗")
    print("║          SISTEMA DE VIAJE COMPARTIDO           ║")
    print("╚════════════════════════════════════════════════╝\n")
    
    print("Ingrese la cantidad de personas:")
    cantidad_personas = validarPositivo()
    
    print("Ingrese los kilómetros a recorrer:")
    kilometros = validarPositivo()
    
    print("Ingrese el consumo del auto (km por litro):")
    consumo = validarPositivo()
    
    print("Ingrese el precio por litro de combustible:")
    precio_litro = validarPositivo()
    
    costo_combustible = calcularCombustible(kilometros, consumo, precio_litro)
    print(f"\nCosto de combustible : ${costo_combustible:.2f}")
    
    print("Ingrese la cantidad de peajes a pasar:")
    cant_peajes = int(validarPositivo())
    costo_peajes = calcularPeajes(cant_peajes)
    print(f"\nCosto de peajes: ${costo_peajes:.2f}")
    
    print("Ingrese la cantidad de días del viaje:")
    dias = validarPositivo()
    
    print("Ingrese el presupuesto diario por persona para comidas:")
    presupuesto_diario = validarPositivo()
    
    costo_comidas = calcularComidas(cantidad_personas, dias, presupuesto_diario)
    print(f"\nCosto en comidas: ${costo_comidas:.2f}")
    
    print("Ingrese la cantidad de noches de alojamiento:")
    noches = validarPositivo()
    
    print("Ingrese el precio por noche:")
    precio_noche = validarPositivo()
    
    costo_alojamiento = calcularAlojamiento(noches, precio_noche)
    print(f"\nCosto total de alojamiento: ${costo_alojamiento:.2f}")
    
    total_sin_descuento = costo_combustible + costo_peajes + costo_comidas + costo_alojamiento
    
    total_con_descuento = aplicarDescuento(total_sin_descuento, cantidad_personas)
    
    pago_por_persona = dividirGastos(total_con_descuento, cantidad_personas)
    
    mostrarResumen(costo_combustible, costo_peajes, costo_comidas, costo_alojamiento, 
                   total_sin_descuento, total_con_descuento, pago_por_persona, cantidad_personas)
    
    print("Gracias!!! y Buen viaje! 🚗")

      
if __name__ == "__main__":
    main()