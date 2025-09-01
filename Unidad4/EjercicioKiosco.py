"""
Un kiosco vende chocolates a $50 cada uno. 
Si un cliente compra 4 chocolates y además paga un 10% de impuesto sobre el total, 
calcular cuánto debe pagar.
"""
chocolates = 10
precio = 100
impuesto = 0.12

total = chocolates * precio + chocolates * precio * impuesto
print("Total a cobrar:", total)