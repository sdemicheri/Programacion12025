"""
Se desea comprar una PC y una impresora. Calcular el precio total: 
el cual está dado por la suma de los precios de costos, los porcentajes de ganancia del vendedor 
y un 21% de IVA.Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora.
Se leen los costos y se imprimen el precio total de ventas.

"""
costo_pc = float(input("Ingrese el costo de la PC: "))
costo_impresora = float(input("Ingrese el costo de la impresora: "))

ganancia_pc = costo_pc * (12/100)
ganancia_impresora = costo_impresora * (7/100)
iva_pc = (costo_pc + ganancia_pc) * (21/100)
iva_impresora = (costo_impresora + ganancia_impresora) * (21/100)
precio_total = (costo_pc + ganancia_pc + iva_pc) + (costo_impresora + ganancia_impresora + iva_impresora)

print(f"El precio total de la venta es: {precio_total:.2f}")