tabla=[[0]*3 for f in range(3)]
acum=0
for f in range (3):
    for c in range(3):
        tabla[f][c]=int(input())
        acum+=tabla[f][c]

prom=acum/9
acum=0
for f in range (3):
    for c in range (3):
        if tabla[f][c]>prom:
            acum+=1

print(acum)
