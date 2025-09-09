"""
SIMULAR UNA CALCULADORA SIMPLE
"""
try:
 número_1 = float (input("Ingrese el primer número: "))
 número_2 = float (input("Ingrese el segundo número: "))
 print("Ingrese una operación: + ,  - ,  * ,  / ")
 operación = input()
 if operación != "+" and operación != "-" and operación != "*" and operación != "/":
  print("La operación ingresa no es valida")
 else:
  if operación == "+":
   print(f"El resultado de la suma es: {número_1 + número_2}")
  elif operación == "-":
   print(f"El resultado de la resta es: {número_1 - número_2}")
  elif operación == "*":
   print(f"El resultado de la multiplicación es: {número_1 * número_2}")
  elif operación == "/" and número_2 != 0:
   print(f"El resultado de la división es: {número_1 / número_2}")
  else:
   print("No se puede dividir por cero")
except ValueError:
 print("Los datos ingresados son erróneos")