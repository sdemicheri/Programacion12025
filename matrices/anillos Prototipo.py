d=int(input("Introducir Dimension: "))
tabla=[[0]*d for f in range(d)]
for f in range (d):
    for c in range(d):
        if f==0 or c==0 or f==d-1 or c==d-1:
            tabla[f][c]=1

if d%2!=0:  #Impar (un centro)
    tabla[d//2][d//2]=1
else:       #Par (cuatro centros)
    tabla[d//2][d//2]=1
    tabla[d//2][d//2-1]=1
    tabla[d//2-1][d//2]=1
    tabla[d//2-1][d//2-1]=1


for i in range (d):
    for j in range (d):
        if tabla[i][j]>=d:
            print(tabla[i][j],end=" ") 
        else:
            print(' '+str(tabla[i][j]), end=' ')
    print()
