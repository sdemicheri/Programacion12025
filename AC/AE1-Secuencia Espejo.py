c=int(input())
while c!=0:
    seguir=False
    num1=''
    num2=''
    indicacion=input()+' '
    
    for i in range (len(indicacion)):
        if seguir==False:
                num1+=indicacion[i]
                if indicacion[i+1]==" ":
                    seguir=True
        elif indicacion[i]!=" ":
            num2+=indicacion[i]

    estructura=num1
    num1=int(num1)
    num2=int(num2)
    while num1<num2:
        num1+=1
        estructura+=str(num1)

    estEspejada=estructura

    for i in range (len(estructura)-1, -1, -1):
        estEspejada+=estructura[i]

    print(estEspejada)

    c-=1