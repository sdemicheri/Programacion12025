# Ejercicio de la Calculadora básica

try:
    num1 = int(input("Ingresa num1:"))
    num2 = int(input("Ingresa num2:"))
    operador= input("Ingrese el simbólo de un operador:")
    if operador == "+":
        suma = num1 + num2
        print("El resultado de la suma es:", suma)
    elif operador == "-":
        resta = num1 - num2
        print("El resultado de la resta es:", resta)
    elif operador == "/":
        if num2 != 0:
            division = num1 / num2
        else:
            print("ERROR")
        print("El resultado de la division es:", division)
    elif operador == "*":
        multiplicacion = num1 * num2
        print("El resultado de la múltiplicaion es:", multiplicacion)
except ValueError:
    print("ERROR al ingresar los número")



