try:

    comida = int(input("Ingrese el total de la comida: "))
    bebidaSA = int(input("Ingrese el total de la bebida sin alcohol: "))
    bebidaCA = int(input("Ingrese el total de la bebida con alcohol: "))
    invitados = int(input("Ingrese el total de invitados: "))
    importe = comida / invitados + bebidaSA / invitados
    extra = bebidaCA / bebidaCA
    if extra == 0:
        print("No hay personas que consuman alcohol.")
    else:
        print("El importe extra por el consumo de alcohol es: ", extra)
    
    print("El importe que debe abonar cada invitado es de: ", importe)

except ValueError:
    print("Los datos ingresados son erroneos."
          "\nPor favor vuelva a intentarlo solo con valores numericons")