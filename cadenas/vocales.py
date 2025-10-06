#ingrese una frase y determine cuantas vocales tiene
contador=0
cad=input().lower()
for i in range (len(cad)):
    if cad[i]=='a' or cad[i]=='e' or cad[i]=='i' or cad[i]=='o' or cad[i]=='u':
        contador+=1
print (contador)
