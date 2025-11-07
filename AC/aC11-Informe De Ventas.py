anio=[0]*13
mes=1
montoMax=0
mesMax=0
while mes!=0:
    mes=int(input())
    if mes!=0:
        monto=int(input())
        if monto>montoMax:
            montoMax=monto
            mesMax=mes
        anio[mes]+=1

for mes in range (1,len(anio)):
    if anio[mes]!=0:
        print('Mes:', mes)
        print('Ventas:', anio[mes])

print('Mayor importe de venta, Mes ', mesMax)