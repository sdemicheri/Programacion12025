"""
Confeccionar un algoritmo que de una frase ingresada, 
determine la cantidad de palabras que contiene.
"""
frase = input("Ingrese una frase: ")
contador_palabras = 1

for i in range(len(frase)):
    if frase[i] == " ":
        contador_palabras += 1

print("La cantidad de palabras es: ",contador_palabras)