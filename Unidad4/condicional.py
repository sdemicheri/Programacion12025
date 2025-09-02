try: 
    comida = int(input("Ingese el total de la comida:"))
    bebida_sa = int(input("Ingrese el total de las bebidas sin alcohol"))
    bebida_ca = int(input("Ingrese el total de las bebidas con alcohol"))
    invitados = int(input("Ingrese el total de invitados: "))
    invitados_ca = int(input("Ingrese el total de invitados que beben alcohol: "))
    importe = comida/invitados + bebida_sa/invitados
    if (invitados_ca > 0): 
        extra = bebida_ca/invitados_ca
        print("El importe extra : ", extra)
    else:
        print("No hay invitados que consuman alcohol")
    print("El importe que debe abonar cada invitado es de : ", importe)    
except ValueError:
    print("Datos incorrectos")