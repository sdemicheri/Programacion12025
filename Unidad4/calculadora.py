try:
    numero1=float(int(input("ingrese primer numero:")))
    operador=input("ingrese el opereador:(+, *, /, -):")
    numero2=float(int(input("ingrese el segundo numero:")))
    if operador == "+":
        resulatadosuma=numero2+numero1
        print(resulatadosuma)
    elif operador == "-":
        resultadoresta=numero1-numero2
        print(resultadoresta)
    elif operador == "*" :
        resultadomultiplicacion=numero1*numero2
        print(resultadomultiplicacion)
    elif operador == "/":
        if numero2 != 0:
            resultadodivision=numero1/numero2
            print(resultadodivision)
        else:
            print("Nose puede dividir por cero")
except ValueError: 
    print("Dato ingresado no valido")