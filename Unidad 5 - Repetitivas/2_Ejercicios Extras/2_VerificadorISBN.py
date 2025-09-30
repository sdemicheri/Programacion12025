"""
ENTRADA:
Numero de dígitos a verificar

PROCESO:
Pedir nro de 10 dígitos
Separar cada dígito del numero completo
Multiplicar cada dígito por su posición, EXCEPTO EL 2
El resultado de cada multiplicación acumularlo 
Verificar si el nro verificador es correcto, que se obtiene mediante verificador = suma % 11

SALIDA:
código verificador (2)
"""
numero = int(input("Ingrese el número de 10 dígitos : ")) #9684443242

suma = 0
contador = 9

for i in range(0,10,1):
    digitos = numero % 10
    numero = numero // 10

    if i >= 1:
        multiplicacion = (digitos * contador)
        suma += multiplicacion # SUMA FINAL = 178
    
    contador -= 1 
   
print (f"El verificador es: {suma % 11}") #, resto = 2