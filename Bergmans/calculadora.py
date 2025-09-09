try: 
    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacion == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacion == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacion == '/':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("No se puede dividir por cero ")
    else:
        print("Operacion no valida, debe asignar alguna operacion ")
except ValueError:
    print("Debes ingresar un valor ") 