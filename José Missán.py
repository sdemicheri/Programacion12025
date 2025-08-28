"""
ENTRADA:
Denominación de cada billete disponible
Precio del peluche

PROCESO:
Leer el precio del peluche con el mensaje "Hola Lu, ingresa el precio del peluche: ${}"
Calcular cuantos billetes de cada denominación se necesita y actualizar el precio restante del peluche
(billete_100=precio_peluche//100
precio_peluche=precio_peluche%100
.....)
Escribir cuantos billetes de cada denominación se necesita con el mensaje: "{} billetes de ${}"

SALIDA:
Cantidad de billetes de cada denominación que necesita
"""
precio_peluche=int(input("Hola Lu, ingresa el precio del peluche: $"))

billete_100=precio_peluche//100
precio_peluche=precio_peluche%100
billete_50=precio_peluche//50
precio_peluche=precio_peluche%50
billete_20=precio_peluche//20
precio_peluche=precio_peluche%20
billete_10=precio_peluche//10
precio_peluche=precio_peluche%10
billete_5=precio_peluche//5
precio_peluche=precio_peluche%5
billete_1=precio_peluche

print(billete_100,"billetes de $100")
print(billete_50,"billetes de $50")
print(billete_20,"billetes de $20")
print(billete_10,"billetes de $10")
print(billete_5,"billetes de $5")
print(billete_1,"billetes de $1")