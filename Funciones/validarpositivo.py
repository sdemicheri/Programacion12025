#Función 1: validarPositivo()

#Responsable: Estudiante A
#Descripción: Solicita un número y valida que sea mayor a 0.
#Entrada: Ninguna (solicita datos por teclado)
#Salida: Retorna el número válido ingresado
#Lógica: Usar estructura repetitiva (while o do-while) para seguir pidiendo el número hasta que sea mayor a 0
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

validarPositivo()