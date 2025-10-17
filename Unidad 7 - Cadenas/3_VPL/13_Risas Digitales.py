"""
las risas digitales más divertidas son aquellas en las que las secuencias de vocales 
son las mismas cuando se leen en el orden natural (de izquierda a derecha) 
o en orden inverso (de derecha a izquierda), ignorando las consonantes. 
Por ejemplo, "hahaha" y "huaauhahhuahau" están entre las risas más divertidas, 
mientras que "riajkjdhhihhjak" y "huehuehue" no están entre las más divertidas.
"""
risa = input("Ingrese una cadena riendose: ")

vocales = ""
vocales_invertida = ""

for i in range(0,len(risa),1):
    if risa[i] == "a" or risa [i] == "e" or risa[i] == "i" or risa[i] == "o" or risa[i] == "u":
        vocales += risa[i]

for j in range(len(vocales)-1,-1,-1):
    vocales_invertida += vocales[j]

if vocales == vocales_invertida:
    print("S")
else:
    print("N")