InvitadosAlcohol=True
alcohol=True
try:
    comida=int(input("ingrese el total de la comida"))
    bebidaSA=int(input("ingrese el total de la bebida sin alcohol"))
    bebidaCA=int(input("ingrese el total de la con alcohol"))
    invitados=int(input("ingrese el total de invitados"))
    invitadosCA=int(input("ingrese el total de invitados que tomen alcohol"))
    importe= comida/invitados+bebidaSA/invitados
    if invitadosCA==0:
        InvitadosAlcohol=False
    else:    
        extraCA= bebidaCA/invitadosCA
    if bebidaCA==0:
        alcohol=False
except ValueError or ZeroDivisionError:
    print("Ingrese los valores en numeros por favor")
except ZeroDivisionError:
    print("Si no hay invitados: Nadie tiene que pagar!")
else:
    print ("El total a pagar de cada uno es de: $", importe)
    if InvitadosAlcohol==True and alcohol==False:
        print("No hay alcohol para los que consumen, o no les cuesta nada")
    elif InvitadosAlcohol==False and alcohol==True:
        print ("No hay nadie que consuma y pague el alcohol")
    else:
        print ("Los que tomaran alcohol pagaran aparte: $", extraCA, "o en total: $", extraCA+importe)
finally:
    print ("usar por garcia")