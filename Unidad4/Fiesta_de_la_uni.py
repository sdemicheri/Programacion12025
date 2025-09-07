comida = int(input("Ingrese el total de la comida:"))
bebida_sa = int(input("Ingrse el total de la bebida sin alcohol:"))
bebida_ca = int(input("Ingrese el total de la bebida con alcohol:"))
invitados = int(input("Ingrse la canridad de invitados:"))
invitados_ca = int(input("Ingrese el total de invitados que beben alcohol:"))
importe = comida/invitados+bebida_sa/invitados
if ( invitados_ca > 0 ):
    extra = bebida_ca/invitados_ca
    print("El importe extra por el consumo de alcohol:" , extra)
else:
    print("No hay personas que consuman alcohol.")
print("El importe que debe abonar cada invitado es de:", importe)
    