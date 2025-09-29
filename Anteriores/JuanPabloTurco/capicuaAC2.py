#Desarrollar un programa que solicite al usuario el ingreso de un número entero de tres cifras y determine si dicho número es capicúa (es decir, que se lee igual de izquierda a derecha que de derecha a izquierda).
#El programa deberá contemplar los siguientes casos especiales:
#Si el usuario no ingresa ningún valor, se debe mostrar el mensaje: "Error al ingresar los datos"
#Si el número ingresado es negativo, se debe mostrar el mensaje:: "El numero debe ser mayor a 0"
#Si el número tiene más o menos de tres cifras, se debe mostrar el mensaje: "El numero debe ser de 3 cifras"
#En caso de que el número cumpla con las condiciones, el programa deberá indicar si el mismo "Es capicua" o "No es capicua"

#Entrada: Numero.
#Proceso: Pedir numero
# Comprobar si es positivo o de 3 cifras y mostrar lo oportuno segun el caso
# Si no hay problema: definir si es capicua
# Mostrar el resultado.
#Salida: Confirmacion de numero capicua /o/ pedir un numero positivo /o/ pedir un numero de 3 cifras.

try:
    num=int(input())
    if num>=0:
        if len(str(num))==3:
            num1=num//100
            num3=(num%100)%10
            if num1==num3:
                print("Es capicua")
            else:
                print("No es capicua")
        else:
            print("El numero de ser de 3 cifras") #mal ahi profe
    else:
        print("El numero debe ser mayor a 0")
except ValueError:
    print("Error en el ingreso de los datos")
