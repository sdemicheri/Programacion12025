"""
Desarrollar un programa que solicite al usuario el ingreso de un numero entero de tres cifras 
y determine si dicho numero es capicua.

Si el usuario no ingresa ningún valor, se debe mostrar el mensaje: "Error al ingresar los datos"

Si el numero ingresado es negativo, se debe mostrar el mensaje:: "El numero debe ser mayor a 0"

Si el numero tiene más o menos de tres cifras, se debe mostrar el mensaje: "El numero debe ser de 3 cifras"

En caso de que el numero cumpla con las condiciones, el programa deberá indicar si el mismo "Es capicua" o "No es capicua"
"""
try:
    numero = int(input("Ingrese un numero de tres cifras: "))

    if numero < 0:
        print("El numero debe ser mayor a 0")
    elif numero < 100 or numero > 999:
        print("El numero debe ser de 3 cifras")
    else:
        unidad = numero % 10
        centena = numero // 100
        if unidad == centena:
            print("Es capicua")
        else:
            print("No es capicua")

except ValueError:
    print("Error en el ingreso de los datos")