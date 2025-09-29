#Función 3: calcularPeajes()

#Responsable: Estudiante C
#Descripción: Calcula el costo total de peajes.
#Entrada: Cantidad de peajes a pasar
#Salida: Retorna el costo total de peajes
#Lógica: Usar estructura repetitiva para pedir el precio de cada peaje y sumarlos.

def calcularPeajes(cantidad):  
    costo_total = 0
    for i in range(cantidad):
        peajes = float(input("Ingrese el monto:"))
        costo_total += peajes
    return costo_total

resultado = calcularPeajes(2)
print(resultado)


