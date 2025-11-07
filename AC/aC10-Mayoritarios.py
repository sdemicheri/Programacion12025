vec=[0]*100
vecAuxiliar=[0]*100
mayoritario=0
mayoritarioCant=0
cantNum= int(input())
vec=input().split()
for i in range (cantNum):
    vecAuxiliar[int(vec[i])]+=1
    
for i in range (100):
    if mayoritarioCant<vecAuxiliar[i]:
        mayoritario=i
        mayoritarioCant=vecAuxiliar[i]

if mayoritarioCant > cantNum/2:
    print(mayoritario)
else:
    print('No hay mayoritario')