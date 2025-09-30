"""
Escribir un programa que permita calcular el precio de un artículo para un año dado,
considerando que la inflación es del 4 por 100 anual.
"""

precio_actual=float(input("ingrese el precio del articulo: "))
año_actual=int(input("ingrese el año actual: "))
año_futuro=int(input("ingrese el año futuro: "))

precio_final = precio_actual*(1+(4/100))**(año_futuro-año_actual)

print (f"el precio del articulo para el año {año_futuro} es {precio_final:.2f}")