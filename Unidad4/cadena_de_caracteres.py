"""""
frase = input ("Ingrese una frase: ")
vocales = ""
for i in range(len(frase)):
    if frase[i].lower() == "a" or frase[i].lower() == "e" or frase[i].lower() == "i" or frase[i].lower() == "o" or frase[i].lower() == "u":
        vocales = vocales + frase[i]
print(len(vocales))
"""
#Sin Vocales
"""""
cadena = input("Ingrese una frase: ")
consonantes = ""
for i in range(len(cadena)):
    if cadena[i].lower() != "a" and cadena[i].lower() != "e" and cadena[i].lower() != "i" and cadena[i].lower() != "o" and cadena[i].lower() != "u":
        consonantes = consonantes + cadena[i]
print(consonantes)
"""
#Ultima Letra
"""
palabra = input("Ingrese una frase: ")
ultima = palabra[-1]
letra_repetida = 0
for i in range(len(palabra)):
    if palabra [i].lower() == ultima.lower():
        letra_repetida += 1
print(letra_repetida)
"""
#Contar Letras (sin espacio)
"""
palabra = input("Ingrese una frase: ")
palabra_sin_espacio = 0
for i in range(len(palabra)):
    if palabra[i] != " ":
        palabra_sin_espacio += 1
print(palabra_sin_espacio)
"""

#Ejercicio con Nota: Confeccionar un algoritmo que de una frase ingresada, determine la cantidad de palabras que contiene.
"""
frase = input("Ingrse una frase: ")
palabras = 1
for i in range(len(frase)):
    if frase[i] == " ":
        palabras += 1
print(palabras)
"""

#Ejercicio URL
""""
url = input("Ingrese la URL: ")
posicion = 0

for i in range(len(url)):
    if url[i] == "/":
        posicion = i + 1

for i in range(len(url)-1):
    if url[i] == "/" and url[i+1] == "/": 
        posicion1 = i
print(url[posicion1 + 2:posicion])
"""
#Palabra mas larga
""""
frase1 = input("Ingrese la primer frase ")
frase2 = input("Ingrese la segunda frase ")
if len(frase1) ==  len(frase2):
    print(frase1) and print(frase2)
elif len(frase1) > len(frase2):
    print(frase1)
else:
    print(frase2)
"""
#Encriptar
""""
cadena = input("Ingrese una frase: ")
posicion = ""

for i in range (0,len(cadena),2):
    if len(cadena) > i + 1:
        posicion += cadena[i + 1]
    posicion += cadena[i]
    
print(posicion)
"""

#AC_MENSAJE
""""
original = input()
oculto = ""
for i in range(len(original)):
    if i == 0: 
        oculto = oculto + original[i]  
    if original[i] == " ":          #Primer letra
        oculto = oculto + original[i+1]
print(oculto)
"""

#AC_Formate Númerico
"""
total = input()
sin_coma = ""
for i in range(len(total)):
    if total[i] == " ":
        sin_coma += "."
    else:
        sin_coma += total[i]
print(sin_coma)
"""

#Risas digitales
"""
risa = input("Ingrese la risa: ")
vocales = ""
for i in range(len(risa)):
    if risa[i] == "a" or risa[i] == "e" or risa[i] == "i" or risa[i] == "o" or risa[i] == "u":
        vocales += risa[i]
invertida = ""
for i in range(len(vocales)-1,-1,-1):
    invertida += vocales[i]
    if invertida == vocales:
        print("S")
    else:
        print("N")
"""
#Oración danzante
""""
oracion = input("Ingrese la oración: ")
danzante = " "
mayuscula = True
for i in range(len(oracion)):
    if oracion[i] == " ":
        danzante += " "
    else:
        if mayuscula == True:
            danzante += oracion[i].upper()
            mayuscula = False
        else:
            danzante += oracion[i].lower()
            mayuscula = True
print(danzante,end="")
"""

#AC 9 Palabra mas larga
'''
frase = input("")

palabra = ""
mas_larga = ""

for i in range(len(frase)):
    if frase[i] != " ":
        palabra += frase[i]
    else:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
        palabra = ""

if len(palabra) > len(mas_larga):
    mas_larga = palabra

print(mas_larga)
'''
