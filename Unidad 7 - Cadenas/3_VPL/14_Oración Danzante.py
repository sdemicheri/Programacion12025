"""
Una oración se considera danzante si su primera letra es mayúscula 
y el caso de cada letra subsiguiente es inverso al de la letra anterior. 
Se deben ignorar los espacios al determinar el caso de una letra. 
"""

cadena = input("Ingrese una cadena: ")
cadena_transformada = ""

print(len(cadena))
for j in range(0,len(cadena),2):
    cadena_transformada += cadena[j].upper()
    if j != len(cadena)-1:
        cadena_transformada += cadena[j+1].lower()

print(cadena)
print(cadena_transformada)