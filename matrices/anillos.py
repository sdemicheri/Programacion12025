columna=int(input("columna"))
fila=int(input("fila"))
tabla=[[1]*fila for i in range(columna)]

#for f in range (fila):
#    for c in range(columna):
#        print('Fila: ', f,'   Columna: ', c)
#        tabla[f][c]=int(input('introducir valor'))

suma=0

maximof=fila-1
maximoc=columna-1
minimo=0
for i in range (3):
    for f in range (fila):
        for c in range(columna):
            if f==minimo or f==maximof or c==minimo or c==maximoc:
                suma+=tabla[f][c]
    print (suma)
    suma=0
    minimo+=1
    maximof-=1
    maximoc-=1