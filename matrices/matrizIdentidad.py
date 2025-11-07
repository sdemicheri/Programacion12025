tabla=[[0]*10 for f in range(10)]
identidad=True

n=int(input())

for f in range(n):
    for c in range(n):
        tabla[f][c]=int(input())

for f in range(n):
    for c in range(n):
        if f==c and tabla[f][c]!=1:
            identidad=False
        elif f!=c and tabla[f][c]!=0:
            identidad=False

if identidad==True:
    print("Es Matriz Identidad")
else:
    print("No Es Matriz Identidad")