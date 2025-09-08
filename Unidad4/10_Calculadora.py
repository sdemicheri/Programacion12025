try:
 numero1 = float(input("Ingrese el primer numero: "))
 numero2 = float(input("Ingrese el segundo numero: "))
 operacion = input("Ingrese la operacion (+,-,x,/): ")
 if operacion == "+":
  suma = numero1 + numero2
  print("resultado:", suma)
 elif operacion == "-":
  resta = numero1-numero2
  print("resultado:", resta)
 elif operacion == "x":
  multiplicacion = numero1*numero2
  print("resultado:", multiplicacion)
 elif operacion != "+" or operacion != "-" or operacion != "x" or operacion != "/":
  print("Ingrese el operador correcto.")
 try:
  if operacion == "/":
   division = numero1 / numero2
   print("resultado:", division)
 except ZeroDivisionError:
  print("No se puede dividir por 0")
except ValueError:
 print("Ingrese los datos correctos.")