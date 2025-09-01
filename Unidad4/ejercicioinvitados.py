comida = int(input("ingrese el total de la comida "))
bebida_sa = int(input("ingrese el total de la bebida sin alcohol  "))
bebida_ca = int(input("ingrese el total de la bebida con alcohol "))
invitados= int(input("ingrese el total de invitados "))
invitados_ca = int(input("ingrese el total de invitados que beben alcohol "))
importe = comida/invitados+bebida_sa/invitados
extra = bebida_ca/invitados_ca
print("el importe que debes abonar cada invitado es de: ", importe)
print("el importe extra por el consumo de alcohol: ", extra)