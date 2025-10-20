frase=input()+" "
contador=0
mayorCantidadDeLetras=0
palabra=""
for i in range (len(frase)):
    if frase[i]!=" ":
            contador+=1
    else:
        contador=0
    if contador>mayorCantidadDeLetras:
        mayorCantidadDeLetras=contador
contador=0

for i in range (len(frase)):
    if frase[i]!=" " and frase[i]!="." and frase[i]!="," and frase[i]!="(" and frase[i]!=")": #hasta ahí
            contador+=1
            palabra+=frase[i]
    elif contador==mayorCantidadDeLetras:
        print(palabra)
        palabra=""
        contador=0
    else:
        palabra=""
        contador=0
