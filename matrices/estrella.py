d=int(input("Introducir Dimension: "))
tabla=[[" "]*d for f in range(d)]
cosa=d

for f in range (d):
    for c in range(d):
        if f==c or c==d//2 or f==d//2:
            tabla[f][c]="*"
#        if f==c:

for i in range (d):
    tabla[i][cosa-1]="*"
    cosa+=-1


for i in range (d):
    for j in range (d):
        print(tabla[i][j],end=" ") 
    print()