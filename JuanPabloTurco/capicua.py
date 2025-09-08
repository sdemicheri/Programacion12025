#Desarrollar un programa que solicite al usuario el ingreso de un número entero de tres cifras y determine si dicho número es capicúa (es decir, que se lee igual de izquierda a derecha que de derecha a izquierda).
#El programa deberá contemplar los siguientes casos especiales:
#Si el usuario no ingresa ningún valor, se debe mostrar el mensaje: "Error al ingresar los datos"
#Si el número ingresado es negativo, se debe mostrar el mensaje:: "El numero debe ser mayor a 0"
#Si el número tiene más o menos de tres cifras, se debe mostrar el mensaje: "El numero debe ser de 3 cifras"
#En caso de que el número cumpla con las condiciones, el programa deberá indicar si el mismo "Es capicua" o "No es capicua"
try:
    a=int(input())
    b=int(input())
except ValueError:
    if a==3:
        print("si")

