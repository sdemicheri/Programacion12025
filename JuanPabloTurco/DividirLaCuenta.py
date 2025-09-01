try:
    comida=int(input("ingrese el total de la comida"))
    bebidaSA=int(input("ingrese el total de la bebida sin alcohol"))
    bebidaCA=int(input("ingrese el total de la con alcohol"))
    invitados=int(input("ingrese el total de invitados"))
    invitadosCA=int(input("ingrese el total de invitados que tomen alcohol"))
except ValueError:
    print("Ingrese los valores en numeros por favor")
else:
    importe= comida/invitados+bebidaSA/invitados
    extraCA= bebidaCA/invitadosCA
    print ("El total a pagar de cada uno es de: $", importe)
    print ("Los que tomaran alcohol pagaran aparte: $", extraCA, "o en total: $", extraCA+importe)
finally:
    print ("usar por garcia")