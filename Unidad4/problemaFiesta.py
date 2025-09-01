try: 
    comida = int(input("Ingese el total de la comida:"))
    bebida_sa = int(input("Ingrese el total de las bebidas sin alcohol"))
    bebida_ca = int(input("Ingrese el total de las bebidas con alcohol"))
    invitados = int(input("Ingrese el total de invitados: "))
    invitados_ca = int(input("Ingrese el total de invitados que beben alcohol: "))
    importe = comida/invitados + bebida_sa/invitados
    try: 
        extra = bebida_ca/invitados_ca
    except ZeroDivisionError:
        extra = 0
        print("No hay invitados que consuman alcohol")
    else: 
        print("El importe extra : ", extra)
    print("El importe que debe abonar cada invitado es de : ", importe)    
except ValueError:
    print("Datos incorrectos")
