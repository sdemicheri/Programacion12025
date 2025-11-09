"""
Una oración se considera danzante si su primera letra es mayúscula 
y el caso de cada letra subsiguiente es inverso al de la letra anterior. 
Se deben ignorar los espacios al determinar el caso de una letra. 
Por ejemplo, "A b Cd" es una oración danzante
 porque la primera letra ('A') es mayúscula, la siguiente ('b') es minúscula, 
 la siguiente ('C') es mayúscula y la siguiente ('d') es minúscula.

Entrada
La entrada una línea que contiene una cadena de texto. 
Esta cadena contendrá entre 1 y 50 caracteres ('A'-'Z', 'a'-'z' o espacio ' '), 
ambos inclusive, o al menos una letra ('A'-'Z', 'a'-'z').

Salida
Convierta la oración en una oración danzante (como en los siguientes ejemplos) 
cambiando el caso de las letras donde sea necesario. 
Se deben conservar todos los espacios en la oración original, es decir, "oración" 
debe convertirse en "SeNtEnCe".
"""
cadena = input("Ingrese una cadena: ")
cadena_transformada = ""

print(len(cadena))
for j in range(0,len(cadena),2):
    cadena_transformada += cadena[j].upper()
    if j != len(cadena)-1:
        cadena_transformada += cadena[j+1].lower()

print(cadena_transformada)