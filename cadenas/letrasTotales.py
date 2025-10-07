contador=0
cad=input().lower()
for i in range (len(cad)):
    if cad[i]!=' ':
        contador+=1
print (contador)