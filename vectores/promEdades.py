acum=0
edades=[0]*10
contador=0
for i in range (10):
    edades[i]=int(input())
    acum+=edades[i]
prom=acum/10
print("Promedio General: ", prom)
#print("Edades mayores al promedio:")
for i in range (10):
    if edades[i]>prom:
#        print (edades[i])
        contador+=1
print("Cantidad de Edades mayores al promedio: ",contador)