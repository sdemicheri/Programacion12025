comida=int(input("Ingrese el total de la comida: "))
bebida_sa=int(input("Ingrese el total de la bebida sin alcohol: "))
bebida_ca=int(input("Ingrese el total de la bebida con alcohol: "))
invitados=int(input("Ingrese el total de invitados: "))
invitados_ca=int(input("Ingrese el total de invitados que beben alcohol: "))
importe= comida/invitados+bebida_sa/invitados
try : 
    extra = bebida_ca/invitados_ca
except ZeroDivisionError:
    extra=0
    print("No hay personas que consuman alcohol.")
else:
    print("El importe extra por el consumo de alcohol: ", extra)
print("El importe que debe abonar cada inivitado es de: ", importe)