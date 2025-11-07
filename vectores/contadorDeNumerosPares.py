vecNumPar=[0]*10
numerosP=0
for i in range(10):
    num=int(input())
    if num%2==0:
        numerosP+=1
        vecNumPar[numerosP-1]=i
print("Cantidad: ", numerosP)
print("Numeros:")
for i in range(numerosP):
    print(vecNumPar[i])
