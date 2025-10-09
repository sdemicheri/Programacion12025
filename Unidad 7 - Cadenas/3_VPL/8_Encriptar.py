"""
Encriptar una cadena utilizando el intercambio de las posiciones 
de los caracteres pares por la posision impar anterior. 
Si la cadena tiene una longitud impar, el ultimo caracter no se intercambia.
"""
cadena = input()
nueva_cadena = ""
for i in range(0,len(cadena),2):
    if len(cadena)-1 == i:
        nueva_cadena += cadena[i]
    elif len(cadena)-1 != i:
        nueva_cadena += cadena[i+1]
        nueva_cadena += cadena[i]
print(nueva_cadena)