"""
Un kiosco vende chocolates a $50 cada uno. 
Si un cliente compra 4 chocolates y además paga un 10% de impuesto sobre el total, 
calcular cuánto debe pagar.
"""
chocolates=4
precio=50
impuesto=10/100

subtotal=chocolates*precio
total=subtotal+(subtotal*impuesto)

print("Total a pagar:", total)