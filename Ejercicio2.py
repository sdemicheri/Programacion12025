capital_inicial = float(input("Ingrese la cantidad a invertir "))
interes_anual = float(input("Ingrese el interés anual en % "))
años = int(input("Ingrese el número de años: "))
capital_final = capital_inicial * (1 + interes_anual / 100) ** años
print("El capital obtenido es:", capital_final)



