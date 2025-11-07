palabra=input("Palabra: ")
d=len(palabra)
tabla=[[" "]*d for f in range(d)]

for i in range(d):
    tabla[0][i]=palabra[i]
    tabla[i][0]=palabra[i]

contador=0

for i in range(d-1,-1,-1):
    tabla[d-1][i]=palabra[contador]
    tabla[i][d-1]=palabra[contador]
    contador+=1


print(tabla)


