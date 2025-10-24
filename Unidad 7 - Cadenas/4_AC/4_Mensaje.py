"""
El mensaje original está formado tomando la primera letra de cada palabra. 
Reconstruyan la frase oculta.
Si elijes quien uniera ese pedido unificarías escuchando decir escondido solo lugares ofrecidos guiados 
ruidosos amargos rosados lugares ocultos.
"""
cadena = input("Ingrese una cadena: ")

mensaje = cadena[0]
for i in range(0,len(cadena)):
    if cadena[i] == " ":
        mensaje += cadena[i+1]

print(mensaje)