try:

    comida = int(input("Ingrese el total de la comida: "))
    bebidaSA = int(input("Ingrese el total de la bebida sin alcohol: "))
    bebidaCA = int(input("Ingrese el total de la bebida con alcohol: "))
    invitados = int(input("Ingrese el total de invitados: "))
    invitadosCA = int(input("Ingrese el total de invitados que beben alcohol: "))
    importe = comida / invitados + bebidaSA / invitados
    
    if comida <= 0 or bebidaSA <= 0 or bebidaCA <= 0 or invitados <= 0 or invitadosCA <= 0:
        raise Exception ("Los datos ingresados son erroneos.")

    if invitadosCA > 0:
        extra = bebidaCA / invitadosCA
        print("El importe extra por el consumo de alcohol es: ", extra)
    else:
        print("No hay personas que consuman alcohol.")
    print("El importe que debe abonar cada invitado es de: ", importe)

except ValueError:
    print("Los datos ingresados son erroneos."
          "\nPor favor vuelva a intentarlo solo con valores numericos")
except Exception as error:
    print(error._str_())