try:
    num1 = float(input("Ingrese el primer número: "))
    operacion = input("Ingrese la operación a realizar (+, -, /, *, **): ")
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == "+":
        resultado = num1 + num2
        print("El resultado es: ", resultado)

    elif operacion == "-":
        resultado = num1 - num2
        print("El resultado es: ", resultado)

    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado es: ", resultado)
        else:
            print("No se puede dividir por 0")

    elif operacion == "*":
        resultado = num1 * num2
        print("El resultado es: ", resultado)

    elif operacion == "**":
        resultado = num1 ** num2
        print("El resultado es: ", resultado)

    else:
        print("Operación no válida")

except ValueError:
    print("SINTAX ERROR: No ingresó un número")
