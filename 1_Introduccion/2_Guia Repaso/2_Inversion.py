"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
inversion = float(input("Ingrese la cantidad a invertir: "))
interés = float(input("Ingrese el interés anual: ")) / 100
años = int(input("Ingrese el número de años: "))

capital_obtenido = inversion * (1 + interés) ** años

print(f"El capital obtenido en la inversión es: {capital_obtenido:.2f}")