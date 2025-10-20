frase=" "+input().lower()+" "
palabra=""
primerLetra=0
ultimaLetra=-1
palindroma=True
palindromos=0
primerEspacio=-1
segundoEspacio=-1
for i in range(len(frase)):
    if frase[i]==" " and primerEspacio==-1:
        primerEspacio=i+1
    elif frase[i]==" " and primerEspacio!=-1:
        segundoEspacio=i
    if primerEspacio!=-1 and segundoEspacio!=-1:
        for i in range(primerEspacio,segundoEspacio):
            palabra+=frase[i]
        for i in range (len(frase)):
            if frase[primerLetra]!=frase[ultimaLetra]:
                palindroma==False
            primerLetra+=1
            ultimaLetra-=1
        palabra=""             #borroPalabra
        primerLetra=0
        ultimaLetra=-1
        if palindroma==True:
            palindromos+=1
        palindroma=True
        primerEspacio=-1
        segundoEspacio=-1
print(palindromos)
