"""
El mensaje original está formado tomando la primera letra de cada palabra. Reconstruyan la frase oculta.

Si elijes quien uniera ese pedido unificarías escuchando decir escondido solo lugares ofrecidos 
guiados ruidosos amargos rosados lugares ocultos.
"""

mensajeOriginal = input()
mensajeOculto = mensajeOriginal[0]

for i in range(0, len(mensajeOriginal), 1):
    if mensajeOriginal[i] == " ":
        espacio = i
        mensajeOculto += mensajeOriginal[i+1]

print(mensajeOculto)