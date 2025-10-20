frase= input()+' '
fraseEncriptada=""
pLetra=1

for i in range (len(frase)-1):
    if frase[i]!=" " and frase[i+1]!=" ":
        if pLetra%2!=0:
            fraseEncriptada+=frase[i+1]
            fraseEncriptada+=frase[i]
        pLetra+=1
    elif frase[i+1]==" " and pLetra%2!=0:
        pLetra=1
        fraseEncriptada+=frase[i]
    else:
        pLetra=1      
        fraseEncriptada+=' '
print(fraseEncriptada)

