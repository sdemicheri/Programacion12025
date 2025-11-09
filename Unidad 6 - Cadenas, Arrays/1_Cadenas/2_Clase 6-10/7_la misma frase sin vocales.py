"""
imprimir la misma palabra pero sin vocales
"""
cadena = "casa"
cadena_resultante = ""

for i in range(len(cadena)):
    if cadena[i] != "a":
        cadena_resultante += cadena[i]

print(cadena_resultante)
print("La longitud es: ",len(cadena_resultante))