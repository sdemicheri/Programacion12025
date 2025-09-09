try:
    numero = float(input("ingrese un numero:"))
    operando = input("ingrese el operando:")
    numero2 = float(input("ingrese otro numero:"))
    suma = "+"
    resta = "-"
    multiplicacion = "*"
    division = "/"
    if( operando == suma):
       suma2 = numero + numero2
       print("el resultado es:", suma2)
    elif( operando == resta):
       resta2 = numero - numero2
       print("el resultado es:", resta2)
    elif( operando == multiplicacion):
       multiplicacion2 = numero * numero2
       print("el resultado es:", multiplicacion2)
    elif( operando == division):
       division2 = numero / numero2
       print("el resultado es:", division2)
    else:
       print("no pusiste el signo de el operando")
except ZeroDivisionError:
   print("no se puede dividir por cero")
except ValueError:
   print("no se han puesto numeros")