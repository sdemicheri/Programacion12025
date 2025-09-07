"""
Una juguetearía tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
y calcule el peso total del paquete que será enviado.
"""
payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))

peso_total = (payasos * 112) + (muñecas * 75)

print("El peso total del paquete es:", peso_total, "gramos.")