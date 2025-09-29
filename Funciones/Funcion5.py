#Función 5: calcularAlojamiento()

#Responsable: Estudiante E
#Descripción: Calcula el costo de alojamiento.
#Entrada: Cantidad de noches, precio por noche
#Salida: Retorna el costo total de alojamiento
#Lógica: Multiplicar noches por precio.

def calcularAlojamiento(noches,precio):
    preciototal=noches*precio
    return preciototal

resultado=calcularAlojamiento(3,100)
print(resultado)
