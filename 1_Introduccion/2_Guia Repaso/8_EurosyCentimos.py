"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos
decimales y muestre por pantalla el número de euros y el número de céntimos del precio
introducido.
"""
precio_euros = float(input("ingrese el precio en euros y con dos decimales: "))

euros=((int(precio_euros)))
centimos=int(round((precio_euros-euros)*100))

print("el numero de euros es: ",euros)
print("el numero de centimos es: ",(centimos))