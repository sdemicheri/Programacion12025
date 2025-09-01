comida = int(input("ingrese el total de la comida: "))
b_sa = int(input("ingrese el total de la bebida sin alcohol: "))
b_ca = int(input("ingrese el total de la bebida con alcohol: "))
invi = int(input("ingrese la cantidad de invitados: "))
invi_ca = int(input("ingrese el total de invitados que consumen alcohol: "))
importe = comida/invi+b_sa/invi
try:
    extra = b_ca/invi_ca
except ZeroDivisionError:
    extra = 0
    print("nadie consume alcohol")
else: 
    print ("el Importe extra por el consumo de alcohol: ", extra)
    
print("el importe a abonar de cada inviado es de: ", importe)