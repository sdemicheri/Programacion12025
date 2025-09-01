"""
Un kiosco vende chocolates a $50 cada uno. 
Si un cliente compra 4 chocolates y además paga un 10% de impuesto sobre el total, 
calcular cuánto debe pagar.
"""
chocolates = int(input("Cantidad de chocolates que compro: "))
precio = int(input("Ingrese el precio de cada chocolate"))
impuesto = 0.10
total = chocolates * precio + chocolates * precio * impuesto
print("Total a pagar:", total)