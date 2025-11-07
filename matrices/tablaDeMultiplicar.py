tabla=[[0]*10 for i in range(10)]
for i in range(10):
    tabla[0][i]=i+1
    tabla[i][0]=i+1

for colum in range (1,10):
    for fila in range (1,10):
        tabla[colum][fila]=tabla[0][fila]*tabla[colum][0]


for i in range (10):
    for j in range (10):
        if tabla[i][j]>=10:
            print(tabla[i][j],end=" ") 
        else:
            print(' '+str(tabla[i][j]), end=' ')
    print()