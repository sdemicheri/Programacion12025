contador=0
cad=input().lower()
caracterFinal=cad[-1]
for i in range (len(cad)):
    if cad[i]==caracterFinal:
        contador+=1
print (contador)