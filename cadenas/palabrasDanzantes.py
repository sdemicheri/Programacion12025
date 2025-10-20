oracion=input().lower()
oracionDanzante=""
for i in range (0,len(oracion),2):
    if i != len(oracion)-1:  
        oracionDanzante+=oracion[i].upper()
        oracionDanzante+=oracion[i+1]
    else:
        oracionDanzante+=oracion[i].upper()
print(oracionDanzante)