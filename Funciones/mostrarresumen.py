#Función 8: mostrarResumen()

#Responsable: Estudiante H
#Descripción: Muestra un resumen completo del viaje.
#Entrada: Todos los costos calculados y el monto por persona
#Salida: Imprime en pantalla un resumen formateado
#Lógica: Estructura secuencial para mostrar todos los datos.

import pyttsx3

def hablar(mensaje):

    voz = pyttsx3.init()
    voz.say(mensaje)
    voz.runAndWait()

def mostrarResumen(costo_combustible, costo_peajes, costo_comidas, costo_alojamiento, total_sin_descuento, total_con_descuento, pago_por_persona, cantidad_personas):
    
    hablar("El costo del combustible es de "+ str(costo_combustible))
    hablar("El costo de los peajes"+ str(costo_peajes))
    hablar("El costo de las comidas es de "+ str(costo_comidas))
    hablar("El costo de los alojamientos es de "+ str(costo_alojamiento))
    hablar("El total sin descuento es de "+ str(total_sin_descuento))
    hablar("El total con descuento es de "+ str(total_con_descuento))
    hablar("El costo por persona es de "+ str(pago_por_persona))
    hablar("La cantidad de personas es de "+ str(cantidad_personas))

