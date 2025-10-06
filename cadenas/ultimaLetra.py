contador=0
cad=input().lower()
if cad[-1]!=' ':
    cad+=' '
for i in range (len(cad)):
    if cad[i]==' ':
        contador+=1
print (contador)