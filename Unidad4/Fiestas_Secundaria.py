try:
    comida = int(input("Ingrese el total de la comida "))
    bebida_sa = int(input("Ingrese el total de la bebida sin alcohol: "))
    bebida_ca = int(input("Ingrese el total de la bebida con alcohol: "))
    invitados = int(input("Ingrese el total de invitados: "))
    invitados_ca = int(input("Ingrese el total de invitados que beben alcohol: "))

    importe = comida/invitados+bebida_sa/invitados

if(comida <= 0 or bebida_sin_alcohol <= 0 or bebida_con_alcohol <= 0 or 
invitados <= 0 or invitados_beben_alcohol <= 0 or invitados_beben_alcohol > invitados):
    print("El importe extra por el consumo de alcohol: ", extra)
else:
    Print("No hay personas que consuman de alcohol:" )
print("El importe total que debe abonar cada inivtado es de :", importe)