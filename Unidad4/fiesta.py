try:
    comida=int(input("Ingrese el total de la comida: "))
    bebida_sa=int(input("Ingrese el total de la bebida sin alcohol: "))
    bebida_ca=int(input("Ingrese el total de la bebida con alcohol: "))
    invitados=int(input("Ingrese el total de invitados: "))
    invitados_ca=int(input("Ingrese el total de invitados que beben alcohol: "))
    importe= comida/invitados+bebida_sa/invitados
    if (comida <= 0 or bebida_sa <= 0 or bebida_ca <=0 or invitados_ca <= 0 or invitados <= 0):
        raise Exception("los datos ingresados son erroneos."
                        "los numeros ingresados deben ser positivos") 
    if (invitados_ca > 0):
        extra = bebida_ca/invitados_ca
        print("El importe extra por el consumo de alcohol: ", extra)
    else:
        print("No hay personas que consuman alcohol.")
    print("El importe que debe abonar cada inivitado es de: ", importe)
except ValueError:
    print("Los datos ingresados son erroneos")
except Exception as error:
    print(error.__str__())